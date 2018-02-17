#!/usr/bin/env python3
import collections
import functools
import glob
import hashlib
import itertools
import os
import re
import shutil
import subprocess
import tempfile
import textwrap
import xml.etree.ElementTree

from htmlthingy import Builder, tags, linkcheck
from bs4 import BeautifulSoup


# TODO: move these to htmlthingy
os.makedirs('imagecache', exist_ok=True)

def cache_get(filename):
    cached = os.path.join('imagecache', filename)
    if os.path.exists(cached):
        return cached
    return None

def cache_put(tempfilename, cachefilename):
    os.makedirs('imagecache', exist_ok=True)
    shutil.copy(tempfilename, os.path.join('imagecache', cachefilename))


builder = Builder()
builder.converter.pygments_style = 'friendly'


def _create_sidebar_thingy(thisfile, maintitle, names, extra=''):
    result = '<div class="sidebarblock">'
    result += '<h3>' + maintitle + '</h3>'
    result += '<ul>'
    for name in names.split():
        result += '<li>'
        titletext = builder.get_title(name + '.txt')
        if name + '.txt' == thisfile:
            result += '<b>' + titletext + '</b>'
        else:
            result += '<a href="%s.html">%s</a>' % (name, titletext)
        result += '</li>'
    result += '</ul>'
    result += extra
    result += '</div>'
    return result


def get_sidebar_content(txtfile):
    if txtfile == 'index.txt':
        indexlink = ''
    else:
        indexlink = '<h3><a href="index.html">Back to front page</a></h3>'

    thingy = functools.partial(_create_sidebar_thingy, txtfile)
    return ''.join([
        thingy("Interesting for programmers",
               'infinity numbertheory fib derivatives geometry-and-trig'),
        thingy("Kinda fun", 'integrals more-integrals'),
        thingy("Mathy", 'more-derivatives more-geometry-and-trig explog'),
        thingy("Mind-blowing", 'taylor eulerformula'),
        thingy("Other stuff", 'basics graphs summary', indexlink),
    ])

builder.get_sidebar_content = get_sidebar_content


builder.get_head_extras = lambda filename: '''
<script type="text/x-mathjax-config">
  // awesome, i have javascript inside html inside python
  MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
      inlineMath: [ ['$','$'] ],
      displayMath: [ ['$$','$$'] ],
    },
    "HTML-CSS": { availableFonts: ["TeX"] }
  });
</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mat\
hjax/2.7.2/MathJax.js"></script>
<link href="https://fonts.googleapis.com/css?family=Cabin|Quicksand" rel="styl\
esheet">
'''


@builder.converter.add_inliner(r'\\\*')
def escaped_star(match, filename):
    return r'*'


# this is really just a convenience thing
@builder.converter.add_multiliner(r'^math:')
def multiline_math(match, filename):
    math = textwrap.dedent(match.string[match.end():]).strip()

    # allow line continuations with \ but insert \\ elsewhere
    lines = (line.replace('\\\n', ' ')
             for line in re.split(r'(?<!\\)\n', math))
    yield r'$$\begin{align}%s\end{align}$$' % (r' \\' + '\n').join(lines)


# for multiline code inside a graybox, pygments hard-codes too much
@builder.converter.add_multiliner(r'^darkcode:(.*)\n')
def dark_code(match, filename):
    code = textwrap.dedent(match.string[match.end():])
    html = tags.multiline_code(code, match.group(1).strip() or 'text',
                               builder.converter.pygments_style)
    soup = BeautifulSoup(html, 'html.parser')
    first_div = soup.find('div')
    first_div['style'] = first_div['style'].replace('#f0f0f0', '#a9a9a9')
    return str(soup)


@builder.converter.add_multiliner(r'^asymptote(3d)?:(.*)\n')
def asymptote(match, filename):
    format = 'png' if match.group(1) else 'svg'     # 3d svg's dont work :(
    code = textwrap.dedent(match.string[match.end():])
    svgfilename = hashlib.md5(code.encode('utf-8')).hexdigest() + '.' + format
    os.makedirs(os.path.join(builder.outputdir, 'asymptote'), exist_ok=True)
    outfile = os.path.join(builder.outputdir, 'asymptote', svgfilename)

    if cache_get(svgfilename) is None:
        with tempfile.TemporaryDirectory() as tmpdir:
            for file in glob.glob('asymptote/*.asy'):
                shutil.copy(file, tmpdir)

            with open(os.path.join(tmpdir, 'image.asy'), 'w') as file:
                file.write('import boilerplate%s;\n' % (match.group(1) or ''))
                file.write(textwrap.dedent(match.string[match.end():]))

            subprocess.check_call(
                ['asy', '-f', format, '--libgs=', 'image.asy'], cwd=tmpdir)
            cache_put(os.path.join(tmpdir, 'image.' + format), svgfilename)

    shutil.copy(cache_get(svgfilename), outfile)

    if format == 'svg':
        # figure out the correct size (lol)
        attribs = xml.etree.ElementTree.parse(outfile).getroot().attrib
        assert attribs['width'].endswith('pt')
        assert attribs['height'].endswith('pt')
        size = (float(attribs['width'][:-2]),
                float(attribs['height'][:-2]))
        extrainfo = 'width="%.0f" height="%.0f"' % size
    else:
        extrainfo = ''

    htmlfile = builder.infile2outfile(filename)
    relative = os.path.relpath(outfile, os.path.dirname(htmlfile))

    html = tags.image(relative.replace(os.sep, '/'), match.group(2))
    return html.replace('<img', '<img %s class="asymptote"' % extrainfo, 1)


# TODO: don't hard-code width and height?
@builder.converter.add_multiliner(r'^canvasdemo:\n')
def canvasdemo(match, filename, *,
               idcounts=collections.defaultdict(lambda: itertools.count(1))):
    canvas_id = 'canvas' + str(next(idcounts[filename]))
    code = "var screen = new CanvasWrapper(%r);\n\n" % canvas_id
    code += textwrap.dedent(match.string[match.end():])

    jsfile = os.path.join(builder.outputdir, 'canvaswrapper.js')
    htmlfile = builder.infile2outfile(filename)
    relative = os.path.relpath(jsfile, os.path.dirname(htmlfile))

    yield ('<script type="text/javascript" src="%s"></script>'
           % relative.replace(os.sep, '/'))
    yield ('<canvas id="%s" width="600" height="400" tabindex="1"></canvas>'
           % canvas_id)
    yield '<script>'
    yield code
    yield '</script>'
    yield "<p>Here's the code:</p>"
    yield tags.multiline_code(code, 'javascript',
                              builder.converter.pygments_style)


@builder.converter.add_inliner(r'\bcanvaswrapper.js\b')
def canvaswrapper_link(match, filename):
    return ('<a href="https://github.com/Akuli/math-tutorial/blob/master/'
            'canvaswrapper.js">canvaswrapper.js</a>')


builder.run()
subprocess.call(['dot', 'chaptergraph.gv', '-T', 'svg',
                 '-o', os.path.join('html', 'chaptergraph.svg')])
linkcheck.run(builder.outputdir)

# tell github pages to do the right thing
open(os.path.join(builder.outputdir, '.nojekyll'), 'x').close()
