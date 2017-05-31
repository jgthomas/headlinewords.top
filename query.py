

import sqlite3
import datetime as dt

from constants import DATABASES


TODAY = dt.datetime.today().date()
THIS_YEAR = TODAY.year


def date_object_factory(start, num_days, plus=None):
    if plus:
        new_date = start + dt.timedelta(days=num_days)
    else:
        new_date = start - dt.timedelta(days=num_days)
    return new_date


TIME_MAP = {"today": TODAY,
            "week": date_object_factory(TODAY, 7),
            "month": date_object_factory(TODAY, 30)}


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

    def __enter__(self):
        self.conn = sqlite3.connect(self.dbname,
                               detect_types=sqlite3.PARSE_DECLTYPES
                               |sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def ondate(self, date):
        if date in TIME_MAP:
            date = TIME_MAP[date]
        self.cur.execute(self.__class__.SPECIFIC_DATE, (date,))
        return self.cur.fetchall()

    def since(self, date):
        if date in TIME_MAP:
            date = TIME_MAP[date]
        self.cur.execute(self.__class__.SINCE_DATE, (date,))
        return self.cur.fetchall()

    def between(self, date1, date2):
        if date1 in CALENDAR_MAP:
            date1 = CALENDAR_MAP[date1]
            date2 = CALENDAR_MAP[date2]
        self.cur.execute(self.__class__.DATE_RANGE, (date1, date2))
        return self.cur.fetchall()

    def single_word(self, date, word):
        if date in TIME_MAP:
            date = TIME_MAP[date]
        self.cur.execute(self.__class__.WORD_ON_DATE, (date, word))
        return self.cur.fetchall()

    def ever(self):
        self.cur.execute(self.__class__.OVERALL_TOTAL)
        return self.cur.fetchall()


def data(dbname, method, date1=None, date2=None, word=None):
    db = DATABASES[dbname]
    with Query(db) as opendb:
        if date1 and date2:
            data = getattr(opendb, method)(date1, date2)
        elif date1 and word:
            data = getattr(opendb, method)(date1, word)
        elif date1:
            data = getattr(opendb, method)(date1)
        else:
            data = getattr(opendb, method)
    return data
