#
# This file is part of Brazil Data Cube Documentation.
# Copyright 2026 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
#

import sphinx_rtd_theme
import sphinx_nefertiti
from unittest.mock import MagicMock

import os
import sys

sys.path.insert(0, os.path.abspath("../../"))


# -- Project information -----------------------------------------------------

project = 'wlts.py'
copyright = 'GNU General Public License, v3.0.'
author = "Brazil Data Cube (BDC)"
autosummary_generate = False
release = '1.0.4'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

autodoc_mock_imports = []


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'sphinx_design',
    "sphinx_rtd_theme",
    'sphinx_colorschemed_images',
    "sphinx_nefertiti",
]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'LICENSE']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_nefertiti"
html_static_path = ['_static']

html_theme_options = {
    # Font settings (these are supported)
    "sans_serif_font": "open sans",
    "documentation_font": "open sans",
    "monospace_font": "fira code",
    "project_name_font": "nunito",
    "doc_headers_font": "nunito",
    "documentation_font_size": "1rem",
    "monospace_font_size": "0.9375rem",

    # Style and color settings (these are supported)
    "style": "blue",  # Options: blue, darkblue, purple, green, etc.
    "pygments_light_style": "pastie",
    "pygments_dark_style": "dracula",

    # Navigation and layout (these are supported)
    "header_links": [
        {"text": "Home", "link": "index"},
        {"text": "BIG", "link": "https://data.inpe.br/", "target": "_blank"},
        {"text": "BDC", "link": "https://data.inpe.br/bdc/", "target": "_blank"},
    ],

    # Logo settings (these are supported)
    "logo": "logo-bdc2.svg",
    "logo_width": 65,
    "logo_height": 65,
    "logo_alt": "BDC/INPE",

    # Footer settings (these are supported)
    "footer_links": [
        {"text": "Documentação BDC", "link": "https://brazil-data-cube.github.io/index.html"},
        {"text": "GitHub", "link": "https://github.com/brazil-data-cube/"},
        {"text": "Discord", "link": "https://discord.gg/enS8GdY6"},
    ],

    # Repository settings (these are supported)
    "repository_url": "https://github.com/brazil-data-cube/wlts.py",
    "repository_name": "wlts.py",
    "docs_repository_url": "https://github.com/brazil-data-cube/wlts.py/tree/main/docs/sphinx/",
}

html_css_files = [
    "custom.css",
]

html_logo = "_static/logo-bdc.png"

html_favicon = "_static/favicon.ico"


copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: '
copybutton_prompt_is_regexp = True

doctest_global_setup = '''
import os
WLTS_EXAMPLE_URL = os.getenv('WLTS_EXAMPLE_URL', None)
'''

#todo_include_todos = True
#todo_emit_warnings = True
master_doc = 'index'
