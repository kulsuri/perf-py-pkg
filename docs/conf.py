"""Sphinx configuration."""
import importlib.metadata

# Path setup
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime


sys.path.insert(0, os.path.abspath("../.."))

# Project information.
project = "Perfect Python Package"
author = "Kulraj Suri"
copyright = f"{datetime.now().year}, Kulraj Suri"
version = importlib.metadata.version("perf_py_pkg")
release = importlib.metadata.version("perf_py_pkg")

extensions = [
    "sphinx.ext.autodoc",  # automatically generate documentation for modules
    "sphinx.ext.napoleon",  # to read Google-style or Numpy-style docstrings
    "sphinx.ext.viewcode",  # to allow vieing the source code in the web page
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
