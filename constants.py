

import datetime as dt

from funcs import date_object


TODAY = date_object()
YESTERDAY = TODAY - dt.timedelta(days=1)
WEEK = TODAY - dt.timedelta(days=7)
MONTH = TODAY - dt.timedelta(days=30)

DATABASE = 'data/headline_words.db'

DATE = dt.datetime.today().strftime("%d_%m_%Y")

NAME = 'headline_words.json'

TODAYS_WORDS = '_'.join([DATE, NAME])

URL = 'http://feeds.bbci.co.uk/news/uk/rss.xml'

IGNORE = ['and', 'a', 'if', 'on', 'no', 'yes', 'by', 'for', 'to', 'in',
          'is', 'are', 'be', 'or', 'as', 'where', 'when', 'how', 'the',
          'off', 'say', 'with', 'what', 'our', 'can', 'not', 'say',
          'says', 'over', 'just', 'that', 'do', 'does', 'from']

SHORT_WORD = 2

TOP_WORDS = 10
