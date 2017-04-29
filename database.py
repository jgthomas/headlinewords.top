#!/usr/bin/env python


import sqlite3
import json
import datetime as dt

from funcs import load_words


DATABASE = 'data/headline_words.db'

conn = sqlite3.connect(DATABASE, 
                        detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = conn.cursor()


def create_table():
    conn.execute('CREATE TABLE IF NOT EXISTS hw(word TEXT, count INTEGER, date DATE)')


def close_up():
    conn.close()


def date_object():
    """ Return date object for today with only year, month and day. """
    now = dt.datetime.now()
    today = dt.date(now.year, now.month, now.day)
    return today


# Basic query strings
base = 'SELECT word, SUM(count), date as "[date]" FROM hw'
total = 'GROUP BY word ORDER BY SUM(count) DESC' 
date = 'WHERE "[date]"=?'
since = 'WHERE "[date]">?'
timespan = 'WHERE "[date]">? AND "[date]"<?'

# Compound query strings
overall_total = ' '.join([base, total])
specific_date = ' '.join([base, date, total])
since_date = ' '.join([base, since, total])
date_range = ' '.join([base, timespan, total])


def query(sql, opts=None):
    if opts:
        cur.execute(sql, opts)
    else:
        cur.execute(sql)
    return cur.fetchall()


TODAY = date_object()
YESTERDAY = dt.date(2017, 4, 28)
TWOBACK = dt.date(2017, 4, 27)
THREEBACK = dt.date(2017, 4, 26)


def add_words(words, date=TODAY):
    for data in words:
        word, count = data
        data_to_add = (word, count, date)
        conn.execute('INSERT INTO hw VALUES (?,?,?)', data_to_add)


create_table()

DATE = dt.datetime.today().strftime("%d_%m_%Y")
NAME = 'headline_words.json'
TODAYS_WORDS = '_'.join([DATE, NAME])


#WORDS = load_words(TODAYS_WORDS)

with conn:
    print(query(since_date, (TWOBACK,)))

close_up()
