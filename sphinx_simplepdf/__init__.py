from sphinx_simplepdf.directives.ifbuilder import IfBuilderDirective
from sphinx_simplepdf.directives.ifinclude import IfIncludeDirective
from sphinx_simplepdf.directives.pdfinclude import PdfIncludeDirective
from pathlib import Path

ROOT_PATH = Path(__file__).parent

def setup(app):
    app.add_directive('if-builder', IfBuilderDirective)
    app.add_directive('if-include', IfIncludeDirective)
    app.add_directive('pdf-include', PdfIncludeDirective)
    app.add_message_catalog("sphinx", ROOT_PATH / "locale")

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
