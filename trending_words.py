

from operator import itemgetter

from constants import BBC_DATABASE, NYT_DATABASE, TOP_N_WORDS, SHORT_N_WORDS, DATABASES

from query_database import (query, TODAY, TOMORROW, DATE_RANGE,
                            date_object_factory, just_words)

ONE_DAY = 1
DAY_ON_DAY = 1
WEEK_ON_WEEK = 7
MONTH_ON_MONTH = 30

TREND_MAP = {"day_on_day": DAY_ON_DAY,
             "week_on_week": WEEK_ON_WEEK,
             "month_on_month": MONTH_ON_MONTH}


def trim_data(data):
    """ Remove date objects to simplify processing. """
    trimmed = []
    for word, count, *_ in data:
        trimmed.append([word, count])
    return trimmed


def successive_periods(db, days):
    """
    Return two database queries for two successive, days, weeks
    months, etc.

    db   :  the database to query
    days :  the number of days each period should be

    Example:
    Returns two lists from the BBC database: the first is
    the frequencies of all words over the last seven
    days, the second the frequencies of all words
    over the previous seven days.
    >>> successive_periods(BBC_DATABASE, WEEK_ON_WEEK)

    """
    one_back = date_object_factory(TOMORROW, days + ONE_DAY)
    pivot = date_object_factory(one_back, ONE_DAY, plus=True)
    two_back = date_object_factory(one_back, days)
    this_period = query(db, DATE_RANGE, (one_back, TOMORROW))
    last_period = query(db, DATE_RANGE, (two_back, pivot))
    return (last_period, this_period)


def changing_counts(last_period, this_period):
    changes = []
    last = trim_data(last_period)
    this = trim_data(this_period)
    last_map = {word: count for word, count in last} 
    this_map = {word: count for word, count in this} 

    # Negative counts for words in last period but not this
    for key, value in last_map.items():
        temp = []
        if key not in this_map:
            temp.append(key)
            temp.append(value * -1)
        if temp:
            changes.append(temp)

    # Positive counts for new entries this period
    for key, value in this_map.items():
        temp = []
        if key not in last_map:
            temp.append(key)
            temp.append(value)
        else: # Change for words found in both periods
            temp.append(key)
            temp.append(this_map[key] - last_map[key])
        if temp:
            changes.append(temp)

    rising_words = [entry for entry in changes if entry[1] > 0]
    falling_words = [entry for entry in changes if entry[1] < 0] 
    rising_words.sort(key=itemgetter(1), reverse=True)
    falling_words.sort(key=itemgetter(1))
    return (rising_words, falling_words)


def main(db, days):
    last_period, this_period = successive_periods(db, days)
    rising, falling = changing_counts(last_period, this_period)
    return (rising, falling)


def trends(db, days):
    db = DATABASES[db]
    days = TREND_MAP[days]
    last_period, this_period = successive_periods(db, days)
    rising, falling = changing_counts(last_period, this_period)
    return (rising, falling)


BBC_DAY_TREND_UP, BBC_DAY_TREND_DOWN = main(BBC_DATABASE, DAY_ON_DAY)
BBC_WEEK_TREND_UP, BBC_WEEK_TREND_DOWN = main(BBC_DATABASE, WEEK_ON_WEEK)

NYT_DAY_TREND_UP, NYT_DAY_TREND_DOWN = main(NYT_DATABASE, DAY_ON_DAY)
NYT_WEEK_TREND_UP, NYT_WEEK_TREND_DOWN = main(NYT_DATABASE, WEEK_ON_WEEK)
