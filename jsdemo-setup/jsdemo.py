# see also: ../asymptote-setup/asymptote.py
import os
import shutil

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.nodes import set_source_info


THIS_PLACE = os.path.abspath(os.path.dirname(__file__))


class jsdemo(nodes.Part, nodes.Element):
    pass


def html_visit_jsdemo(self, node):
    shutil.copy(os.path.join(THIS_PLACE, 'canvaswrapper.js'),
                self.builder.outdir)
    self.body.append(self.starttag(node, 'div', CLASS='i'))

    # FIXME: support multiple demos in same file
    code = "var screen = new CanvasWrapper('canvas1');\n\n" + node['code']
    width = node.get('width', '400')
    height = node.get('height', '600')

    html = '''
    <script type="text/javascript" src="canvaswrapper.js"></script>
    <canvas id="canvas1" width="%s" height="%s" tabindex="1"></canvas>
    <script>%s</script>
    </div>      <!-- this finishes self.starttag above -->
    <p>Here's the code:</p>
    ''' % (width, height, code)
    self.body.append(html)

    # this is based on sphinx/writers/html.py
    highlighted = self.highlighter.highlight_block(
        code, 'javascript', opts={}, linenos=False,
        #location=(self.builder.current_docname, node.line),    # flake8: noqa
    )
    starttag = self.starttag(node, 'div', suffix='',
                             CLASS='highlight-javascript')
    self.body.append(starttag + highlighted + '</div>\n')

    raise nodes.SkipNode


class JSDemoDirective(Directive):

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'width': int, 'height': int}

    def run(self):
        node = jsdemo()
        node['code'] = '\n'.join(self.content)
        node['width'] = self.options.get('width', '600')
        node['height'] = self.options.get('height', '400')
        node['docname'] = self.state.document.settings.env.docname
        set_source_info(self, node)
        if hasattr(self, 'src'):
            node.source = self.src
        return [node]


def setup(app):
    app.add_node(jsdemo, html=(html_visit_jsdemo, None))
    app.add_directive('jsdemo', JSDemoDirective)
