
CONF_TEMPLATE = """
import os
import sys
sys.path.insert(0, os.path.abspath('{repo_path}'))

project = '{project_name}'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme'
]
templates_path = ['_templates']
exclude_patterns = {excluded}
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
"""

INDEX_CONTENT = """
Welcome to {project_name}'s documentation!
==============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. automodule:: {project_name}
    :members:
    :undoc-members:
    :show-inheritance:
"""