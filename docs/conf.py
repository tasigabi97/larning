import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "latexpy"
copyright = "2020, peti"
author = "peti"

release = "1"

extensions = ["sphinx.ext.autodoc"]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "classic"

html_static_path = ["_static"]

autodoc_default_options = {"member-order": "bysource", "special-members": True, "private-members": True, "exclude-members": "__weakref__"}
latex_elements = {"extraclassoptions": "openany,oneside"}
html_theme_options = {"relbarbgcolor": "black"}
