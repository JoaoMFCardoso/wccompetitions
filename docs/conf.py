Python
# Configuration file for the Sphinx documentation builder.
project = 'wccompetitions'
copyright = '2026, João Cardoso'
author = 'João Cardoso'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster' # Or 'sphinx_rtd_theme' if you install it
html_static_path = ['_static']
