"FPDF for python"
__license__ = "LGPL 3.0"
__version__ = "1.7"
__all__ = ['HTMLMixin', 'Template', 'FPDF']

from .template import Template
from .fpdf import FPDF

try:
    from .html import HTMLMixin
except ImportError:
    import warnings
    warnings.warn("web2py gluon package not installed, required for html2pdf")

