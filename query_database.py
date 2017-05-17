#!/usr/bin/env python


import sqlite3
import datetime as dt

from constants import (BBC_DATABASE,
                       NYT_DATABASE,
                       TOP_N_WORDS,
                       SHORT_N_WORDS)


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

    Example:
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


def word_counts(db, word, dates):
    """
    Return the number of times a single word was used
    on each of the supplied dates.

    db    : the database to query
    word  : the target word
    dates : Python date objects from which to get word counts

    Example: searching for 'election' over the last week
    >>> word_counts(BBC_DATABASE, 'election', [date objects for each day])
    >>> [1, 3, 0, 4, 6, 7, 2]

    Where each number represents the frequency of the word
    'election' on each of the last seven days.

    """
    counts = []
    for date in dates:
        for _, count, _ in query(db, word_on_date, (date, word)):
            if count:
                counts.append(count)
            else:
                counts.append(0)
    return counts


def just_words(data):
    """
    Return just the words from a query to the database,
    discarding the counts and dates, as these are not
    required for some outlets like Alexa.

    """
    words = []
    for word, *rest in data:
        words.append(word)
    return words


def date_object():
    """ Return date object for today with year, month and day. """
    now = dt.datetime.now()
    return dt.date(now.year, now.month, now.day)


def date_object_factory(start, num_days):
    """ Return a date object for num_days prior to start. """
    return start - dt.timedelta(days=num_days)


def date_object_range(start, days):
    """ Return a range of consecutive date objects. """
    day_nums = [n for n in range(days, -1, -1)]
    return [date_object_factory(start, n) for n in day_nums]


# Date objects for database queries
TODAY = date_object()
YESTERDAY = date_object_factory(TODAY, 1)
WEEK = date_object_factory(TODAY, 7)
MONTH = date_object_factory(TODAY, 30)


# Repeated time-based queries #
BBC_TOP = query(BBC_DATABASE, specific_date, (TODAY,))[:SHORT_N_WORDS]
BBC_TODAY = query(BBC_DATABASE, specific_date, (TODAY,))[:TOP_N_WORDS]
BBC_WEEK = query(BBC_DATABASE, since_date, (WEEK,))[:TOP_N_WORDS]
BBC_MONTH = query(BBC_DATABASE, since_date, (MONTH,))[:TOP_N_WORDS]
BBC_EVER = query(BBC_DATABASE, overall_total)[:TOP_N_WORDS]

NYT_TOP = query(NYT_DATABASE, specific_date, (TODAY,))[:SHORT_N_WORDS]
NYT_TODAY = query(NYT_DATABASE, specific_date, (TODAY,))[:TOP_N_WORDS]
NYT_WEEK = query(NYT_DATABASE, since_date, (WEEK,))[:TOP_N_WORDS]
NYT_MONTH = query(NYT_DATABASE, since_date, (MONTH,))[:TOP_N_WORDS]
NYT_EVER = query(NYT_DATABASE, overall_total)[:TOP_N_WORDS]
