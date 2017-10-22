#!/usr/bin/env python3
import collections
import functools
import glob
import hashlib
import itertools
import os
import shutil
import subprocess
import tempfile
import textwrap

from htmlthingy import Builder, tags, linkcheck


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
    for name in names:
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
    result = ''.join([
        thingy("Chapters", ['derivatives', 'integrals', 'geometry-and-trig',
                            'numbertheory']),
        thingy("Other stuff", ['basics', 'explanations'], indexlink),
    ])
    return result

builder.get_sidebar_content = get_sidebar_content


# these are based on sphinx stuff (i.e. copied from sphinx)
BLOCK_MATH_TEMPLATE = r'''
\documentclass[12pt]{article}
\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{anyfontsize}
\usepackage{bm}
\pagestyle{empty}

\begin{document}
\fontsize{12}{14}\selectfont \begin{equation*}
\begin{split}%s\end{split}
\end{equation*}
\end{document}
'''.lstrip()

INLINE_MATH_TEMPLATE = r'''
\documentclass[12pt]{article}
\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{anyfontsize}
\usepackage{bm}
\pagestyle{empty}

\begin{document}
\fontsize{12}{14}\selectfont $%s$
\end{document}
'''.lstrip()


def run_latex(math, textfile, is_inline):
    os.makedirs(os.path.join(builder.outputdir, 'math'), exist_ok=True)
    pngfilename = hashlib.md5(math.encode('utf-8')).hexdigest() + '.png'
    outfile = os.path.join(builder.outputdir, 'math', pngfilename)

    if cache_get(pngfilename) is None:
        with tempfile.TemporaryDirectory() as tmpdir:
            with open(os.path.join(tmpdir, 'math.tex'), 'w') as file:
                template = (INLINE_MATH_TEMPLATE if is_inline
                            else BLOCK_MATH_TEMPLATE)
                file.write(template % math)

            subprocess.check_call(
                ['latex', '--interaction=nonstopmode', 'math.tex'],
                cwd=tmpdir, stdout=subprocess.DEVNULL)
            subprocess.check_call(
                ['dvipng', '-o', 'math.png', '-T', 'tight', '-z9',
                 '-gamma', '1.5',  '-D', '110', '-bg', 'Transparent',
                 'math.dvi'], cwd=tmpdir, stdout=subprocess.DEVNULL)
            cache_put(os.path.join(tmpdir, 'math.png'), pngfilename)

    shutil.copy(cache_get(pngfilename), outfile)
    htmlfile = builder.infile2outfile(textfile)
    relative = os.path.relpath(outfile, os.path.dirname(htmlfile))
    return relative.replace(os.sep, '/')


@builder.converter.add_inliner(r'\B\$(.+?)\$\B')
def inline_math(match, filename):
    path = run_latex(match.group(1), filename, True)
    return '<img class="inlinemath" src="%s" />' % path


@builder.converter.add_multiliner(r'^math:')
def multiline_math(match, filename):
    math = textwrap.dedent(match.string[match.end():])
    path = run_latex(math, filename, False)
    yield '<p><img src="%s" class="blockmath" /></p>' % path


@builder.converter.add_multiliner(r'^asymptote(3d)?:(.*)\n')
def asymptote(match, filename):
    code = textwrap.dedent(match.string[match.end():])
    pngfilename = hashlib.md5(code.encode('utf-8')).hexdigest() + '.png'
    os.makedirs(os.path.join(builder.outputdir, 'asymptote'), exist_ok=True)
    outfile = os.path.join(builder.outputdir, 'asymptote', pngfilename)

    if cache_get(pngfilename) is None:
        with tempfile.TemporaryDirectory() as tmpdir:
            for file in glob.glob('asymptote/*.asy'):
                shutil.copy(file, tmpdir)

            with open(os.path.join(tmpdir, 'image.asy'), 'w') as file:
                file.write('import boilerplate%s;\n' % (match.group(1) or ''))
                file.write(textwrap.dedent(match.string[match.end():]))

            subprocess.check_call(['asy', '-f', 'png', 'image.asy'],
                                  cwd=tmpdir)
            cache_put(os.path.join(tmpdir, 'image.png'), pngfilename)

    shutil.copy(cache_get(pngfilename), outfile)

    htmlfile = builder.infile2outfile(filename)
    relative = os.path.relpath(outfile, os.path.dirname(htmlfile))
    yield tags.image(relative.replace(os.sep, '/'), match.group(2))


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
linkcheck.run(builder.outputdir)

# tell github pages to do the right thing
open(os.path.join(builder.outputdir, '.nojekyll'), 'x').close()
