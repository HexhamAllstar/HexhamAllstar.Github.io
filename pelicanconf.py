#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Phil Bingham'
SITENAME = "Phil's Data Science Portfolio"

PATH = 'content'

TIMEZONE = 'Europe/Paris'
THEME = 'pelican-themes/voidy-bootstrap'
DEFAULT_LANG = 'English'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Download CV', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 10
IPYNB_USE_META_SUMMARY = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

STATIC_PATHS = ['images']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SITESUBTITLE ='A collection of data science/machine learning notebooks and anything else that I find interesting.'

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"
CUSTOM_SIDEBAR_MIDDLES = ("sb_links.html", "sb_taglist.html", )

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"

SOCIAL = (('LinkedIn', 'http://www.linkedin.com/in/philbingham45/',
         'fa fa-linkedin-square fa-fw fa-lg'),
        ('GitHub', 'http://github.com/hexhamallstar',
         'fa fa-github-square fa-fw fa-lg'),
        )
