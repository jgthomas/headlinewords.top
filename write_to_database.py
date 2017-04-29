

import sqlite3
#import datetime as dt
from funcs import load_words, date_object
from constants import DATABASE, TODAYS_WORDS


TODAY = date_object()
WORDS = load_words(TODAYS_WORDS)


conn = sqlite3.connect(DATABASE, 
                        detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)


def create_table():
    conn.execute('CREATE TABLE IF NOT EXISTS hw(word TEXT, count INTEGER, date DATE)')


def add_words(words):
    for data in words:
        word, count = data
        data_to_add = (word, count, FOURBACK)
        conn.execute('INSERT INTO hw VALUES (?,?,?)', data_to_add)


def main():
    with conn:
        create_table()
        add_words(WORDS)
    conn.close()


if __name__ == '__main__':

    main()
