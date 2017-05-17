#!/usr/bin/env python


import sqlite3

from constants import (BBC_DATABASE,
                       NYT_DATABASE,
                       TODAY,
                       WEEK,
                       MONTH,
                       TOP_N_WORDS)


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


### Queries ###
BBC_TOP = query(BBC_DATABASE, specific_date, (TODAY,))[:5]
BBC_TODAY = query(BBC_DATABASE, specific_date, (TODAY,))[:TOP_N_WORDS]
BBC_WEEK = query(BBC_DATABASE, since_date, (WEEK,))[:TOP_N_WORDS]
BBC_MONTH = query(BBC_DATABASE, since_date, (MONTH,))[:TOP_N_WORDS]
BBC_EVER = query(BBC_DATABASE, overall_total)[:TOP_N_WORDS]

NYT_TOP = query(NYT_DATABASE, specific_date, (TODAY,))[:5]
NYT_TODAY = query(NYT_DATABASE, specific_date, (TODAY,))[:TOP_N_WORDS]
NYT_WEEK = query(NYT_DATABASE, since_date, (WEEK,))[:TOP_N_WORDS]
NYT_MONTH = query(NYT_DATABASE, since_date, (MONTH,))[:TOP_N_WORDS]
NYT_EVER = query(NYT_DATABASE, overall_total)[:TOP_N_WORDS]
