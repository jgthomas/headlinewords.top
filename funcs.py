

import json


def load_words(words):
    with open(words, 'r') as infile:
        todays_words = json.load(infile)
    return todays_words
