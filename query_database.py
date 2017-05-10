#!/usr/bin/env python


import sqlite3


# Basic query strings
base = 'SELECT word, SUM(count), date as "[date]" FROM hw'
total = 'GROUP BY word ORDER BY SUM(count) DESC' 
date = 'WHERE "[date]"=?'
since = 'WHERE "[date]">?'
timespan = 'WHERE "[date]">? AND "[date]"<?'
single_word = ' AND word=?'


# Compound query strings
overall_total = ' '.join([base, total])
specific_date = ' '.join([base, date, total])
since_date = ' '.join([base, since, total])
date_range = ' '.join([base, timespan, total])
word_on_date = ' '.join([base, date, single_word])


def query(db, sql, opts=None):
    """ 
    Return query results from the selected database. 
    
    db:   database to query
    sql:  SQL query string
    opts: optional query parameters in the form of a tuple

    Examles:
    >>> from constants import BBC_DATABASE, TODAY
    >>> query(BBC_DATABASE, specific_date, (TODAY,))
    returns word frequencies from todays headlines at the BBC

    """
    conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    with conn:
        if opts:
            cur.execute(sql, opts)
        else:
            cur.execute(sql)
        data = cur.fetchall()
    conn.close()
    return data
