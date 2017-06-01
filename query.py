

import sqlite3
#import datetime as dt
from contextlib import closing

from constants import DATABASES

from query_functions import strip_dates, TIME_MAP, CALENDAR_MAP


class Query(object):    
    
    # Basic query strings
    BASE = 'SELECT word, SUM(count), date as "[date]" FROM hw'
    TOTAL = 'GROUP BY word ORDER BY SUM(count) DESC'
    DATE = 'WHERE "[date]"=?'
    SINCE = 'WHERE "[date]">?'
    TIMESPAN = 'WHERE "[date]">? AND "[date]"<?'
    SINGLE_WORD = ' AND word=?'

    # Compound query strings
    OVERALL_TOTAL = ' '.join([BASE, TOTAL])
    SPECIFIC_DATE = ' '.join([BASE, DATE, TOTAL])
    SINCE_DATE = ' '.join([BASE, SINCE, TOTAL])
    DATE_RANGE = ' '.join([BASE, TIMESPAN, TOTAL])
    WORD_ON_DATE = ' '.join([BASE, DATE, SINGLE_WORD])
    

    def __init__(self, db):
        self.dbname = db
        self.conn = sqlite3.connect(self.dbname,
                               detect_types=sqlite3.PARSE_DECLTYPES
                               |sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def ondate(self, date):
        """ Return counts for all words ON date. """
        if date in TIME_MAP:
            date = TIME_MAP[date]
        self.cur.execute(self.__class__.SPECIFIC_DATE, (date,))
        return self.cur.fetchall()

    def since(self, date):
        """ Return counts for all words SINCE date. """
        if date in TIME_MAP:
            date = TIME_MAP[date]
        self.cur.execute(self.__class__.SINCE_DATE, (date,))
        return self.cur.fetchall()

    def between(self, date1, date2):
        """ Return counts for all words BETWEEN the two dates. """
        if date1 in CALENDAR_MAP:
            date1 = CALENDAR_MAP[date1]
        if date2 in CALENDAR_MAP:
            date2 = CALENDAR_MAP[date2]
        self.cur.execute(self.__class__.DATE_RANGE, (date1, date2))
        return self.cur.fetchall()

    def single_word(self, date, word):
        """ Return count for a SINGLE WORD on date. """
        if date in TIME_MAP:
            date = TIME_MAP[date]
        self.cur.execute(self.__class__.WORD_ON_DATE, (date, word))
        return self.cur.fetchall()

    def ever(self):
        """ Return counts for all words EVER. """
        self.cur.execute(self.__class__.OVERALL_TOTAL)
        return self.cur.fetchall()


def data(dbname, method, date1=None, date2=None, word=None):
    """
    Execute the relevant method from the Query class, using the
    relevant database and parameters.

    dbname  :  database to query
    method  :  method to call for the query
    date1   :  single or first date to query, can be either
               a date object or key to a date object
    date2   :  second date in a query with a range, can be either
               a date object or key to a date object
    word    :  the specific word to query

    """
    db = DATABASES[dbname]
    with closing( Query(db) ) as opendb:
        if date1 and date2:
            data = getattr(opendb, method)(date1, date2)
        elif date1 and word:
            data = getattr(opendb, method)(date1, word)
        elif date1:
            data = getattr(opendb, method)(date1)
        else:
            data = getattr(opendb, method)()
    return strip_dates(data)


def word_count(db, word, dates):
    """
    Return the number of times a single word was used
    on each of the supplied dates.

    db    : the database to query
    word  : the target word
    dates : days to get word counts

    Example: searching for 'election' over the last week
    >>> word_counts('bbc', 'election', [list of date objects])
    >>> [1, 3, 0, 4, 6, 7, 2]

    Where each number represents the frequency of the word
    'election' on each of the last seven days.

    """
    counts = []
    for date in dates:
        for _, count in data(db, "single_word", date, word):
            if count:
                counts.append(count)
            else:
                counts.append(0)
    return counts
