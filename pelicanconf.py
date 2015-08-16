#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Antonino Ingargiola'
SITENAME = u'Single-Molecules Bits'
SITESUBTITLE = u'Of scientific computing and single molecules.'
SITEDESCRIPTION = 'A blog about single-molecules and scientific computing.'
SITEURL = 'http://tritemio.github.io/smbits'
TWITTER_USERNAME = 'tritemio_sc'
DISQUS_SITENAME = 'smbits'
GOOGLE_ANALYTICS = ''

PATH = 'content'
DEFAULT_LANG = u'en'
TIMEZONE = 'America/Los_Angeles'
SLUGIFY_SOURCE = 'basename'
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 50
DISPLAY_PAGES_ON_MENU = True

DIRECT_TEMPLATES = ('index', 'archives')
DEFAULT_LANG = 'en'
#DATE_FORMATS = { 'en': '%B %d, %Y', }
STATIC_PATHS = ['images', 'favicon.ico']
ARTICLE_EXCLUDES = ['.ipynb_checkpoints', '2015-09/.ipynb_checkpoints']

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_METADATA = {
    'status': 'draft',
}

# Blogroll
LINKS = (('Biophysical Society', 'http://www.biophysics.org/'),
         ('Planet Scipy', 'http://planet.scipy.org/'),
)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/tritemio_sc'),
          ('GitHub', 'http://github.com/tritemio'),
          ('ResearchGate', 'https://www.researchgate.net/profile/Antonino_Ingargiola'),
          ('Academia.edu', 'https://ucla.academia.edu/AntoninoIngargiola'),
)

DEFAULT_PAGINATION = 10

THEME = 'notmyidea'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
NOTEBOOK_DIR = 'notebooks'
MARKUP = ['md']

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['render_math', 'ipynb',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           ]

#EXTRA_HEADER = open('_nb_header.html', 'rb').read().decode('utf-8')
