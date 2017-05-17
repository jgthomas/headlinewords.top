#!/usr/bin/env python


import sqlite3
import json
import os.path
from collections import Counter

from query_database import TODAY
from feed_getter import SOURCES
from process_words import get_words, filter_words


HL_FILE = 'headlines.json'
HL_WORDS_FILE = 'headline_words.json'
DB_NAME = 'headline_words.db'
DB_PATH = 'data/'


def save_to_json(filename, words):
    """ Save data to JSON file. """
    with open(filename, 'w') as outfile:
        json.dump(words, outfile)


def load_from_json(filename):
    """ Get data from JSON file. """
    with open(filename, 'r') as infile:
        todays_words = json.load(infile)
    return todays_words


def get_new_headlines(filename, headlines):
    """ 
    Return headlines in the most recent result that 
    were not in the previous. 
    
    """
    if os.path.isfile(filename):
        old_headlines = load_from_json(filename)
        new_headlines = [x for x in headlines if x not in old_headlines]
    else:
        new_headlines = headlines[:]
    return new_headlines


def add_to_database(db, words):
    """ Add the words to the specified database. """
    conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    conn.execute('CREATE TABLE IF NOT EXISTS hw(word TEXT, count INTEGER, date DATE)')
    with conn:
        for data in words:
            word, count = data
            data_to_add = (word, count, TODAY)
            conn.execute('INSERT INTO hw VALUES (?,?,?)', data_to_add)
    conn.close()


def main():
    """
    For each headline source:
    
    1. Pull in the source name and latest headlines. 
    2. Get headlines from the new batch that were not in the previous
    3. Save the newly released headlines to json

    If updated headlines were found:

    1. Get word frequencies for those headlines
    2. Save those frequencies to json, using source appropriate filename
    3. Update the database of words for the current source

    """
    for source in SOURCES:
        name, headlines = source

        headlines_filename = '_'.join([name, HL_FILE])
        new_headlines = get_new_headlines(headlines_filename, headlines)

        save_to_json(headlines_filename, headlines)
        if new_headlines:
            word_frequencies = Counter(filter_words(name, get_words(new_headlines)))
            new_words = word_frequencies.most_common()

            new_words_filename = '_'.join([name, HL_WORDS_FILE])
            save_to_json(new_words_filename, new_words)

            db = '_'.join([name, DB_NAME])
            db_path = ''.join([DB_PATH, db])
            add_to_database(db_path, new_words)


if __name__ == '__main__':

    main()
