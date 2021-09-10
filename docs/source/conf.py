import importlib.util
import os
import sys

# readthedocs generated the whole documentation in an isolated environment
# by cloning the git repo. Thus, any on-the-fly operation will not effect
# on the resulting documentation. We therefore need to import and run the
# corresponding code here.
spec = importlib.util.spec_from_file_location("generate_example_images", "../generate_example_images.py")
generate_example_images = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate_example_images)

# Pre-generate the example images
generate_example_images.main()

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
current_path = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
sys.path.append(current_path)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
    'sphinx_autodoc_defaultargs',
    'sphinx_copybutton',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.youtube',
]

# substitutes the default values
docstring_default_arg_substitution = 'Default: '

bibtex_bibfiles = ['references.bib']
napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.ipynb']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Kornia'
author = f'{project} developers'
copyright = f'2019, {author}'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# version = 'master (' + kornia.__version__ + ' )'
version = ''

if 'READTHEDOCS' not in os.environ:
    # if developing locally, use pyro.__version__ as version
    from kornia import __version__

    version = __version__

# release = 'master'
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'
pygments_dark_style = "monokai"

html_theme = 'furo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "announcement": """
        <a style=\"text-decoration: none; color: white;\"
           href=\"https://github.com/kornia/kornia\">
           <img src=\"_static/img/GitHub-Mark-Light-32px.png\" width=20 height=20/>
           Click here to give a Star to Kornia on GitHub
        </a>
    """,
}

# html_logo = '_static/img/kornia_logo.svg'
html_logo = '_static/img/kornia_logo_only.png'
html_favicon = '_static/img/kornia_logo_favicon.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_extra_path = ['_extra']

# Output file base name for HTML help builder.
htmlhelp_basename = 'Kornia'


# -- Options for LaTeX output ---------------------------------------------

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
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, 'kornia.tex', 'Kornia', 'manual')]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'Kornia', 'Kornia Documentation', [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'kornia',
        'Kornia Documentation',
        author,
        'Kornia',
        'Differentiable Computer Vision in Pytorch.',
        'Miscellaneous',
    )
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('http://numpy.org/doc/stable/', None),
    'torch': ('http://pytorch.org/docs/stable/', None),
}
