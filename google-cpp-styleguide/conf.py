# -*- coding: utf-8 -*-



import sys, os
project = u'Google C++ 開源專案風格指南'
copyright = u''
version = u''
release = u''

source_suffix = '.rst'
master_doc = 'index'
language = 'zh_TW'
exclude_patterns = [
    '_build']
extensions = ['sphinx.ext.imgmath']
pygments_style = 'sphinx'

# on_rtd is whether we are on readthedocs.org
import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify it

html_title = u'Google C++ 開源專案風格指南'
htmlhelp_basename = 'google-cpp-styleguide-zh-tw'
html_add_permalinks = ""

file_insertion_enabled = False
latex_documents = [
  ('index', 'google-cpp-styleguide-zh-tw.tex', u'Google C++ 開源專案風格指南',
   u'', 'manual'),
]


#Add sponsorship and project information to the template context.
context = {
    'MEDIA_URL': "/media/",
    'slug': 'google-cpp-styleguide-zh-tw',
    'name': u'Google C++ 開源專案風格指南',
    'analytics_code': 'None',
}

html_context = context
