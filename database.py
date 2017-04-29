#!/usr/bin/env python


import sqlite3
import json
import datetime as dt

from funcs import load_words, date_object
from constants import DATABASE


conn = sqlite3.connect(DATABASE, 
                        detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = conn.cursor()


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


# For testing to be deleted
TODAY = date_object()
YESTERDAY = dt.date(2017, 4, 28)
TWOBACK = dt.date(2017, 4, 27)
THREEBACK = dt.date(2017, 4, 26)
FOURBACK = dt.date(2017, 4, 25)


def main():
    with conn:
        print(query(overall_total))
        #print(query(specific_data, (YESTERDAY,)))
        #print(query(since_date, (TWOBACK,)))
        #print(query(date_range, (TWOBACK, TODAY)))
    conn.close()


if __name__ == '__main__':

    main()
