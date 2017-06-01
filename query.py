

import sqlite3
import datetime as dt
from contextlib import closing

from constants import DATABASES


TODAY = dt.datetime.today().date()
THIS_YEAR = TODAY.year


def date_of(year, month, day):
    """ Return date object for year, month and day. """
    return dt.datetime(year, month, day).date()


def new_date(start, num_days, plus=False):
    """
    Return new date object for num_days prior to (or after) start.

    start     :  initial date object, often today's date
    num_days  :  number of days prior to start to subtract
    plus      :  option to add days rather than subtract

    """
    if plus:
        new_date = start + dt.timedelta(days=num_days)
    else:
        new_date = start - dt.timedelta(days=num_days)
    return new_date


def strip_dates(data):
    stripped = []
    for word, count, *_ in data:
        stripped.append([word, count])
    return stripped


TIME_MAP = {"tomorrow": new_date(TODAY, 1, plus=True),
            "today": TODAY,
            "yesterday": new_date(TODAY, 1),
            "week": new_date(TODAY, 7),
            "month": new_date(TODAY, 30)}


CALENDAR_MAP = {"jan_start": dt.datetime(THIS_YEAR - 1, 12, 31),
                "jan_end": dt.datetime(THIS_YEAR, 2, 1),
                "feb_start": dt.datetime(THIS_YEAR, 1, 31),
                "feb_end": dt.datetime(THIS_YEAR, 3, 1),
                "mar_start": dt.datetime(THIS_YEAR, 2, 28),
                "mar_end": dt.datetime(THIS_YEAR, 4, 1),
                "apr_start": dt.datetime(THIS_YEAR, 3, 31),
                "apr_end": dt.datetime(THIS_YEAR, 5, 1),
                "may_start": dt.datetime(THIS_YEAR, 4, 30),
                "may_end": dt.datetime(THIS_YEAR, 6, 1),
                "jun_start": dt.datetime(THIS_YEAR, 5, 31),
                "jun_end": dt.datetime(THIS_YEAR, 7, 1),
                "jul_start": dt.datetime(THIS_YEAR, 6, 30),
                "jul_end": dt.datetime(THIS_YEAR, 8, 1),
                "aug_start": dt.datetime(THIS_YEAR, 7, 31),
                "aug_end": dt.datetime(THIS_YEAR, 9, 1),
                "sep_start": dt.datetime(THIS_YEAR, 8, 31),
                "sep_end": dt.datetime(THIS_YEAR, 10, 1),
                "oct_start": dt.datetime(THIS_YEAR, 9, 30),
                "oct_end": dt.datetime(THIS_YEAR, 11, 1),
                "nov_start": dt.datetime(THIS_YEAR, 10, 31),
                "nov_end": dt.datetime(THIS_YEAR, 12, 1),
                "dec_start": dt.datetime(THIS_YEAR, 11, 30),
                "dec_end": dt.datetime(THIS_YEAR + 1, 1, 1)}


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
