#!/usr/bin/env python


import re
import json
import datetime as dt
from collections import Counter

import feedparser

from pythonic_pipes import (is_not_in,
                            filter_by,
                            map_over)

from constants import (URL,
                       TODAYS_WORDS,
                       IGNORE,
                       SHORT_WORD,
                       TOP_WORDS)


def no_numbers(x):
    """ Remove words beginning with a digit. """
    return re.sub(r'^[0-9].+$', '', x)


def no_non_word(x):
    """ Remove non-word characters. """
    return re.sub(r'\W', '', x)


def too_short(x):
    """ Return True if word is too short. """
    return len(x) > SHORT_WORD


def lower(x):
    """ Return x in lowercase. """
    return x.lower()


def get_words(url):
    """
    Pulls down the RSS feed from BBC News and returns 
    all the words found in the headlines.

    """
    feed = feedparser.parse(url)
    headlines = (x['title'].split() for x in feed['entries'])
    headline_words = (word for headline in headlines for word in headline)
    return headline_words


# Maps - apply function to every word
to_lowercase = map_over(lower)
del_non_word_chars = map_over(no_non_word)

# Filters - remove words based on these
remove_function_words = filter_by(is_not_in(IGNORE))
remove_numbers = filter_by(no_numbers)
remove_short_words = filter_by(too_short)


def filter_words(words):
    """
    Transforms the words through application of the 
    maps and filters to every element.

    """
    filtered_words = (del_non_word_chars
                      (remove_short_words
                       (remove_numbers
                        (remove_function_words
                         (to_lowercase(words))))))
    return filtered_words


def save_words(words):
    """ Save the words to a JSON file. """
    with open(TODAYS_WORDS, 'w') as outfile:
        json.dump(words, outfile)


def main():
    word_frequencies = Counter(filter_words(get_words(URL)))
    save_words(word_frequencies.most_common())


if __name__ == '__main__':

    main()
