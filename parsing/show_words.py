#!/usr/bin/env python


import json

from bbc_headlines import TODAYS_WORDS


def load_words(words):
    with open(words, 'r') as infile:
        todays_words = json.load(infile)
    return todays_words


def print_words(words):
    for data in words:
        word, count = data
        print('{} {}'.format(word, count))


def main():
    words = load_words(TODAYS_WORDS)
    print_words(words)
