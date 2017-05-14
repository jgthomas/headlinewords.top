

import datetime as dt

from funcs import date_object


# Words to exclude from the database
STOPWORDS = 'static/wordlists/stopwords.txt'
BBC_STOPWORDS = 'static/wordlists/bbc_stopwords.txt'

# Exclude words shorter than
SHORT_WORD = 2

# Retrieve this many words for queries
TOP_N_WORDS = 10

# Date objects for database queries
TODAY = date_object()
YESTERDAY = TODAY - dt.timedelta(days=1)
WEEK = TODAY - dt.timedelta(days=7)
MONTH = TODAY - dt.timedelta(days=30)

# Databases for each source
BBC_DATABASE = 'data/bbc_headline_words.db'
NYT_DATABASE = 'data/nyt_headline_words.db'
