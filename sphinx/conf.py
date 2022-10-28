# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Configure path to the root directory, i.e. sphinx-python-documentation
import os
import sys
# The path should point to the root directory of the project and looking at the project
# structure, from conf.py we should reach the root by going up two parent directories
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Design Documentation'
copyright = '2022, L. Z.'
author = 'L. Z.'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    #'sphinx_qt_documentation',
    'sphinx.ext.viewcode',
    'rinoh.frontend.sphinx',
]

# python __init__ function is part of the documentation
autodoc_default_options = {
    'special-members': '__init__'
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'navigation_depth': 5,
}
html_css_files = [
    'custom.css',
]

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').

    'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    'preamble': '',
    # Latex figure (float) alignment
    'figure_align': 'htbp',
}

# for external links to standard library
#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3', None),
#    'PyQt5': ('https://www.riverbankcomputing.com/static/Docs/PyQt5/', None),
#}