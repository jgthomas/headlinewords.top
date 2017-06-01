

from operator import itemgetter

from query import data
from query_functions import new_date, strip_dates, TIME_MAP


TREND_MAP = {"day_on_day": 1,
             "week_on_week": 7,
             "month_on_month": 30}


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
    one_back = new_date(TIME_MAP["tomorrow"], days + 1)
    pivot = new_date(one_back, 1, plus=True)
    two_back = new_date(one_back, days)
    this_period = data(db, "between", one_back, "tomorrow")
    last_period = data(db, "between", two_back, pivot)
    return (last_period, this_period)


def changing_counts(last_period, this_period):
    changes = []
    last = strip_dates(last_period)
    this = strip_dates(this_period)
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


def trends(db, days):
    days = TREND_MAP[days]
    last_period, this_period = successive_periods(db, days)
    rising, falling = changing_counts(last_period, this_period)
    return (rising, falling)
