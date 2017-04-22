#!/usr/bin/env python


import re
from collections import Counter

import feedparser

from functional.pythonic_pipes import (lower,
                                       is_not_in,
                                       filter_by,
                                       map_over)


URL = 'http://feeds.bbci.co.uk/news/uk/rss.xml'

IGNORE = ['and', 'a', 'if', 'on', 'no', 'yes', 'by', 'for', 'to', 'in',
          'is', 'are', 'be', 'or', 'as', 'where', 'when', 'how', 'the',
          'off', 'say', 'with', 'what', 'our', 'can']

SHORT_WORD = 3


def no_numbers(x):
    digits = re.compile(r'^[0-9].+$')
    return re.sub(digits, '', x)


def no_non_word_char(x):
    return re.sub(r'\W', '', x)


def too_short(x):
    return len(x) > SHORT_WORD


# Maps
to_lowercase = map_over(lower)
remove_non_word_chars = map_over(no_non_word_char)

# Filters
remove_function_words = filter_by(is_not_in(IGNORE))
remove_numbers = filter_by(no_numbers)
remove_short_words = filter_by(too_short)


feed = feedparser.parse(URL)
headline_feed = feed['entries']
headlines = (x['title'].split() for x in headline_feed)
headline_words = (word for headline in headlines for word in headline)


def filter_words(words):
    filtered_words = (remove_non_word_chars
                      (remove_short_words
                       (remove_numbers
                        (remove_function_words
                         (to_lowercase(words))))))
    return list(filtered_words)

word_frequencies = Counter(filter_words(headline_words))
