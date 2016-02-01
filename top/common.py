# -*- coding: utf-8 -*-

import os
from os.path import dirname, join as pjoin

# Settings
DEBUG = True


# Files and locations
_CUR_PATH = dirname(os.path.abspath(__file__))
BASE_PATH = pjoin(_CUR_PATH, os.pardir, 'static', '')
TEMPLATE_PATH = pjoin(_CUR_PATH, 'templates')
DATA_FILE_TMPL = '{lang}/{project}/{year}/{month}/{day}.json'
DATA_PATH_TMPL = pjoin(BASE_PATH, DATA_FILE_TMPL)
LANG_PROJ_LINK_TMPL = u'http://top.hatnote.com/{lang}/{project}/'
DATE_PERMALINK_TMPL = (u'http://top.hatnote.com/{lang}/{project}/'
                       '{year}/{month}/{day}.html')
PERMALINK_TMPL = (u'http://top.hatnote.com/{lang}/{project}/{year}/{month}/'
                  '{day}.html#title-{title}')
FEED_FILE_TMPL = 'feeds/{lang}{project}.rss'
FEED_PATH_TMPL = pjoin(BASE_PATH, FEED_FILE_TMPL)


# Valuable and important URLs
TOP_API_URL = 'http://wikimedia.org/api/rest_v1/metrics/pageviews/'\
              'top/{lang}.{project}/all-access/{year}/{month}/{day}'
MW_API_URL = 'http://{lang}.{project}.org/w/api.php?'
TOTAL_TRAFFIC_URL = 'https://metrics.wmflabs.org/static/public/'\
                    'datafiles/Pageviews/{lang}{project}.csv'


# Other variables
LOCAL_LANG_MAP = {'en': u'English',
                  'de': u'Deutsch',
                  'fr': u'Français',
                  'ko': u'한국어',
                  'et': u'Eesti',
                  'sv': u'Svenska',
                  'da': u'Dansk',
                  'it': u'Italiano',
                  'ca': u'Català',
                  'es': u'Español',
                  'fa': u'فارسی',
                  'ur': u'اردو',
                  'zh': u'中文',
                  'kn': u'ಕನ್ನಡ',
                  'no': u'bokmål'}
DEFAULT_LANG = 'en'
DEFAULT_PROJECT = 'wikipedia'

ABOUT = '''<p>Learn more on the <a href="#">Hatnote Blog</a>.</p>

<p><a name="about"></a>A daily list of the most visited Wikipedia articles,
generated by <a href="https://twitter.com/sklaporte">Stephen LaPorte</a> and <a
href="https://twitter.com/mhashemi">Mahmoud Hashemi</a>. It's also available in
<a href="http://top.hatnote.com/about.html">more languages</a>. If you find this list
interesting, you will enjoy <a href="http://weekly.hatnote.com">The
Weeklypedia</a>, a weekly digest of the most edited Wikipedia articles.</p>

<p>This page was made possible by <a
href="https://wikimedia.org/api/rest_v1/?doc#!/Pageviews_data/get_metrics_\
pageviews_top_project_access_year_month_day">Wikipedia's
new page view API</a>, with some nice images and summaries from the <a
href="https://www.mediawiki.org/wiki/API:Query">MediaWiki API</a>. You can find
more code and documentation <a href="https://github.com/hatnote/top">available
on github</a>.</p>

<p>Want to see a list of the most visited articles in another language of
Wikipedia? So do we! Please <a href="https://github.com/hatnote/top/\
issues">send
a request</a> and let us know if you can help translate the templates.</p>

<p><a href="https://twitter.com/hatnotable">@hatnotable</a></p>'''

# These prefixes are not for articles
PREFIXES = ['Special', 'Template', 'Sp?cial', 'Project']
