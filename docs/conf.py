# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from docutils import nodes
from docutils.transforms import Transform

# -- Project information -----------------------------------------------------

# Content audience differentiation. You can set an environment variable
# to control the target audience label.
#
# $ export TARGET_AUDIENCE="Campaign"
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    target_audience = os.environ.get('READTHEDOCS_PROJECT').split('-')[-1].title()
else:
    target_audience = os.environ.get('TARGET_AUDIENCE', "Newsroom")
target_audience_lower = target_audience.lower()

rst_prolog = """
.. |target_audience|    replace:: {}
.. |target_audience_lower| replace:: {}
""".format(target_audience, target_audience_lower)

project = u'The Field Guide to Security Training in the {}'.format(target_audience)
copyright = u'2018, OpenNews and contributors (MIT license)'
author = u'OpenNews and contributors (MIT license)'

# The short X.Y version
version = u'1.0.1'
# The full version, including alpha/beta/rc tags
release = u'1.0.1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'training-clipart-blue-button-training-hi.png'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'TheFieldGuidetoSecurityTraininginthe{}doc'.format(target_audience)


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'preamble': "".join((
        '\DeclareUnicodeCharacter{1F407}{*}',  # BunniES!!!
        '\DeclareUnicodeCharacter{200A}{ }',  # hairline space
    )),
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc,
    'TheFieldGuidetoSecurityTraininginthe{}.tex'.format(target_audience),
    u'The Field Guide to Security Training in the {}'.format(target_audience),
    [author],
    'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc,
    'thefieldguidetosecuritytraininginthe{}'.format(target_audience_lower),
    u'The Field Guide to Security Training in the {}'.format(target_audience),
    [author],
    1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc,
    'TheFieldGuidetoSecurityTraininginthe{}'.format(target_audience),
    u'The Field Guide to Security Training in the {}'.format(target_audience),
    author,
    'TheFieldGuidetoSecurityTraininginthe{}'.format(target_audience),
    'This field guide provides training information for the {}.'.format(target_audience),
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- unicode substitutions -- because PDF converter can't handle unicode bunnies

# -- support both RST and Markdown ---
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

# Enables Jinja templating of files prior to rendering.
# http://ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/

global_substitutions = {
  'target_audience': target_audience,
  'target_audience_lower': target_audience_lower,
  }

def render_jinja(app, docname, source):
    """
    Process pages through Jinja for templating.
    """
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.global_substitutions
    )
    source[0] = rendered

def setup(app):
    app.add_config_value(
            'global_substitutions',
            global_substitutions,
            True
            )
    app.connect("source-read", render_jinja)
