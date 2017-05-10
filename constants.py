

import datetime as dt

from funcs import date_object


# Words to exclude from the database
IGNORE = ['and', 'a', 'if', 'on', 'no', 'yes', 'by', 'for', 'to', 'in',
          'is', 'are', 'be', 'or', 'as', 'where', 'when', 'how', 'the',
          'off', 'say', 'with', 'what', 'our', 'can', 'not', 'an',
          'says', 'over', 'just', 'that', 'do', 'does', 'from', 'too',
          'why', 'out', 'mr', 'ms', 'miss', 'mrs', 'dr', 'it']

# Exclude words shorter than
SHORT_WORD = 2

# Retrieve this many words for queries
TOP_WORDS = 10

# Date objects for database queries
TODAY = date_object()
YESTERDAY = TODAY - dt.timedelta(days=1)
WEEK = TODAY - dt.timedelta(days=7)
MONTH = TODAY - dt.timedelta(days=30)

# Databases for each source
BBC_DATABASE = 'data/bbc_headline_words.db'
NYT_DATABASE = 'data/nyt_headlines_words.db'
