# render asymptote images in sphinx
#
# it took me a loooong time to create this thing
# this is based on sphinx/ext/mathbase.py and some other bits of sphinx source
# code because sphinx api documentation is fucking shit, page after page after
# page of reference material, even "tutorials" are just bits of source code
# with some gibberish text in between
import hashlib
import os
import posixpath
import shutil
import subprocess
import tempfile

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.images import Image as ImageDirective
from sphinx.util.nodes import set_source_info


THIS_PLACE = os.path.abspath(os.path.dirname(__file__))


class asymptote(nodes.Part, nodes.Element):
    pass


def render_drawing(self, code):
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = "%s.png" % (hashlib.md5(code.encode('utf-8')).hexdigest())
        relfn = posixpath.join(self.builder.imgpath, 'asymptote', filename)
        outfn = os.path.join(self.builder.outdir, self.builder.imagedir, 'asymptote', filename)
        if os.path.isfile(outfn):
            return relfn

        with open(os.path.join(tmpdir, 'drawing.asy'), 'w') as fuck:
            fuck.write(code)

        for file in os.listdir(THIS_PLACE):
            if file.endswith('.asy'):
                shutil.copyfile(os.path.join(THIS_PLACE, file),
                                os.path.join(tmpdir, file))

        subprocess.check_call(['asy', '-f', 'png', 'drawing.asy'], cwd=tmpdir)
        pngpath = os.path.join(tmpdir, 'drawing.png')

        # Move generated image on tempdir to build dir
        os.makedirs(os.path.dirname(outfn), exist_ok=True)
        # my /tmp and /home are on different drives and shutil.move
        # doesn't seem to move across drives
        shutil.copy(pngpath, outfn)
        return relfn


def html_visit_asymptote(self, node):
    # type: (nodes.NodeVisitor, displaymath) -> None
    fname = render_drawing(self, node['code'])
    self.body.append(self.starttag(node, 'div', CLASS='i'))

    # this is based on looking at the generated html with the inspector
    # the </div>'s end the self.body.append thing above
    # TODO: support alts? it'd be quite pointless though
    if 'align' in node:
        html = '<p><img src="%s" class="align-%s"/></p></div>' % (fname, node['align'])
    else:
        html = '<p><img src="%s"/></p></div>' % fname
    self.body.append(html)
    raise nodes.SkipNode


class AsyDirective(Directive):

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'align': ImageDirective.option_spec['align'],
        '3d': directives.flag,
    }

    def run(self):
        # type: () -> List[nodes.Node]
        node = asymptote()
        node['code'] = (
            ('import boilerplate%s;\n' % ['','3d']['3d' in self.options])
            + '\n'.join(self.content))
        node['docname'] = self.state.document.settings.env.docname
        if 'align' in self.options:
            node['align'] = self.options['align']

        ret = [node]
        set_source_info(self, node)
        if hasattr(self, 'src'):
            node.source = self.src
        #self.add_target(ret)
        return ret


def setup(app):
    app.add_node(asymptote, html=(html_visit_asymptote, None))
    app.add_directive('asymptote', AsyDirective)
