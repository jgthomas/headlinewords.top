#!/usr/bin/env python


import re
import json
import datetime as dt
from collections import Counter

import feedparser

from functional.pythonic_pipes import (is_not_in,
                                       filter_by,
                                       map_over)


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


def no_numbers(x):
    return re.sub(r'^[0-9].+$', '', x)

def no_non_word(x):
    return re.sub(r'\W', '', x)

def too_short(x):
    return len(x) > SHORT_WORD

def lower(x):
    return x.lower()


def get_words(url):
    feed = feedparser.parse(url)
    headlines = (x['title'].split() for x in feed['entries'])
    headline_words = (word for headline in headlines for word in headline)
    return headline_words


# Maps
to_lowercase = map_over(lower)
del_non_word_chars = map_over(no_non_word)

# Filters
remove_function_words = filter_by(is_not_in(IGNORE))
remove_numbers = filter_by(no_numbers)
remove_short_words = filter_by(too_short)


def filter_words(words):
    filtered_words = (del_non_word_chars
                      (remove_short_words
                       (remove_numbers
                        (remove_function_words
                         (to_lowercase(words))))))
    return filtered_words


def save_words(words):
    with open(TODAYS_WORDS, 'w') as outfile:
        json.dump(words, outfile)


def main():
    word_frequencies = Counter(filter_words(get_words(URL)))
    save_words(word_frequencies.most_common())


if __name__ == '__main__':

    main()
