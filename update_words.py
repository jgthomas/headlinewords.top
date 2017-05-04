#!/usr/bin/env python


import sqlite3
import os.path
from collections import Counter

from constants import DATABASE, TODAY
from feed_getter import SOURCES
from funcs import load_words, save_to_json
from bbc_headlines import get_words, filter_words


HL_FILE = 'headlines.json'
HL_WORDS_FILE = 'headline_words.json'
DB_NAME = 'headline_words.db'
DB_PATH = 'data/'


def get_new_headlines(filename, headlines):
    if os.path.isfile(filename):
        old_headlines = load_words(filename)
        new_headlines = [x for x in headlines if x not in old_headlines]
    else:
        new_headlines = headlines[:]
    return new_headlines


def add_to_database(db, words):
    conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    conn.execute('CREATE TABLE IF NOT EXISTS hw(word TEXT, count INTEGER, date DATE)')
    with conn:
        for data in words:
            word, count = data
            data_to_add = (word, count, TODAY)
            conn.execute('INSERT INTO hw VALUES (?,?,?)', data_to_add)
    conn.close()


def main():
    for source in SOURCES:
        name, headlines = source
        headlines_filename = '_'.join([name, HL_FILE])
        new_headlines = get_new_headlines(headlines_filename, headlines)
        save_to_json(headlines_filename, headlines)
        if new_headlines:
            new_words_filename = '_'.join([name, HL_WORDS_FILE])
            db = '_'.join([name, DB_NAME])
            db_path = ''.join([DB_PATH, db])
            word_frequencies = Counter(filter_words(get_words(new_headlines)))
            new_words = word_frequencies.most_common()
            save_to_json(new_words_filename, new_words)
            add_to_database(db_path, new_words)


if __name__ == '__main__':

    main()
