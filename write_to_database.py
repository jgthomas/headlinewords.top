

import sqlite3

from funcs import (load_words,
                   name_factory)

from constants import (DATABASE, 
                       NAME,
                       TODAY)


FILENAME = name_factory(TODAY, NAME)
WORDS = load_words(FILENAME)

conn = sqlite3.connect(DATABASE, 
                        detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)


def create_table():
    conn.execute('CREATE TABLE IF NOT EXISTS hw(word TEXT, count INTEGER, date DATE)')


def add_words(words):
    for data in words:
        word, count = data
        data_to_add = (word, count, TODAY)
        conn.execute('INSERT INTO hw VALUES (?,?,?)', data_to_add)


def main():
    with conn:
        create_table()
        add_words(WORDS)
    conn.close()


if __name__ == '__main__':

    main()
