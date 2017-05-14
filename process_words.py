#!/usr/bin/env python


import re

from pythonic_pipes import (is_not_in,
                            filter_by,
                            map_over)

from constants import STOPWORDS, BBC_STOPWORDS, SHORT_WORD


def get_words(source):
    """ Return all words in the headlines from the source. """
    split_headlines = (x.split() for x in source)
    headline_words = (word for headline in split_headlines for word in headline)
    return headline_words


def starts_with_num_or_non_word(x):
    """ Remove words beginning with a digit or non-word character. """
    return re.sub(r'^[\W0-9].+$', '', x)


def no_non_word(x):
    """ 
    Remove most non-word characters. 
    
    Keeping: hyphen; apostrophe.

    """
    return re.sub(r'[^\w\'-]', '', x)


def no_initial_quote(x):
    """ Remove initial quotation marks. """
    return re.sub(r'^[\'\"]', '', x)


def no_trailing_quote(x):
    """ Remove trailing quotation marks. """
    return re.sub(r'[\'\"]$', '', x)


def too_short(x):
    """ Return True if word is too short. """
    return len(x) > SHORT_WORD


def lower(x):
    """ Return x in lowercase. """
    return x.lower()


def word_filter(words, to_ignore):
    """
    Transforms the words through application of the 
    maps and filters to every element.

    """
    # Maps - apply function to every word
    to_lowercase = map_over(lower)
    del_non_word_chars = map_over(no_non_word)
    del_initial_quote = map_over(no_initial_quote)
    del_trailing_quote = map_over(no_trailing_quote)

    # Filters - remove words based on these
    remove_function_words = filter_by(is_not_in(to_ignore))
    remove_initial_non_letters = filter_by(starts_with_num_or_non_word)
    remove_short_words = filter_by(too_short)

    filtered_words = (del_non_word_chars
                      (remove_short_words
                       (remove_initial_non_letters
                        (remove_function_words
                         (del_trailing_quote
                          (del_initial_quote
                           (to_lowercase(words))))))))
    return filtered_words


def filter_words(source, words):
    """ Set the correct stopwords and filter words. """
    to_ignore = set(line.strip() for line in open(STOPWORDS))
    if source == 'bbc':
        to_ignore = to_ignore.union(set(line.strip() for line in open(BBC_STOPWORDS)))
    return word_filter(words, to_ignore)
