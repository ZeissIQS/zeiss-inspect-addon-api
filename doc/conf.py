# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Add-On Documentation'
copyright = '2023, Carl Zeiss GOM Metrology GmbH'
author = 'Carl Zeiss GOM Metrology GmbH'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_rtd_theme', 'sphinx_favicon', 'sphinx.ext.githubpages', 'sphinx_sitemap', 'sphinxcontrib.newsfeed', 'sphinx_tags']
source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = ['README.md']

tags_create_tags = True
tags_extension = 'md'

myst_enable_extensions = [
  'colon_fence',
  'fieldlist',
  'replacements',
  'deflist',
  'attrs_inline'
]

myst_heading_anchors = 4

# Suppress the warning "WARNING: Non-consecutive header level increase" which commonly appears in python_api/python_api.md
# Unfortunately, suppressing this only for a single file does not seem to work...
suppress_warnings  = ['myst.header']

# -- Options for sitemap -----------------------------------------------------
# https://sphinx-sitemap.readthedocs.io/en/latest/getting-started.html
html_baseurl = 'https://zeissiqs.github.io/zeiss-inspect-addon-api/2023/'
sitemap_url_scheme = "{link}"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# Do not show "View page source" link on every page
html_show_sourcelink = False

#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_theme_options = {
  # Toc options
  'includehidden': False
}

# "sphinx_rtd_theme" appends " &mdash; <project>  documentation" to the page heading -
# this changes the title to "<page_heading> &mdash; <project>"
html_title = project
html_static_path = ['_static']

# -- Override some "sphinx_rtd_theme" styles to match ZEISS branding ---------------
# https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
html_style = "css/theme_zeiss.css"

favicons = [
    {
        "rel": "icon",
        "sizes": "16x16",
        "static-file": "favicon.png",  # => use `_static/favicon.png`
        "type": "image/png",
    }
]

# Source: https://brand.zeiss.com/cmsPublic/brandportal/basic-design-elements/logo-tagline.html
html_logo =  "_static/zeiss-logo-rgb.png"
