#!/usr/bin/env python


import json
import sqlite3
import os.path
from collections import Counter

from constants import DATABASE, TODAY
from feed_getter import SOURCES
from funcs import load_words
from bbc_headlines import get_words, filter_words


HL_FILE = 'headlines.json'
HL_WORDS_FILE = 'headline_words.json'


conn = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)


def save_to_json(filename, words):
    with open(filename, 'w') as outfile:
        json.dump(words, outfile)


def get_new_headlines(filename, headlines):
    if os.path.isfile(filename):
        old_hlines = load_words(filename)
        new_hlines = [x for x in headlines if x not in old_hlines]
    else:
        new_hlines = headlines[:]
    return new_hlines


def add_to_database(words):
    conn.execute('CREATE TABLE IF NOT EXISTS hw(word TEXT, count INTEGER, date DATE)')
    for data in words:
        word, count = data
        data_to_add = (word, count, TODAY)
        conn.execute('INSERT INTO hw VALUES (?,?,?)', data_to_add)


def main():
    for source in SOURCES:
        name, headlines = source
        hl_filename = '_'.join([name, HL_FILE])
        new_hlw_filename = '_'.join([name, HL_WORDS_FILE])
        new_headlines = get_new_headlines(hl_filename, headlines)
        save_to_json(hl_filename, headlines)
        if new_headlines:
            word_frequencies = Counter(filter_words(get_words(new_headlines)))
            save_to_json(new_hlw_filename, word_frequencies.most_common())
            new_words = load_words(new_hlw_filename)
            with conn:
                add_to_database(new_words)
        conn.close()


if __name__ == '__main__':

    main()
