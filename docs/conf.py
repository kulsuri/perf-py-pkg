"""Sphinx configuration."""
project = "Perfect Python Package"
author = "Kulraj Suri"
copyright = "2023, Kulraj Suri"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
