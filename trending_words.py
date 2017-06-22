from operator import itemgetter
from query import data
from query_functions import TOMORROW, new_date, strip_dates, date_spans


TREND_MAP = {"day_on_day": 1,
             "week_on_week": 7,
             "month_on_month": 30}


def successive_periods(db, days):
    """
    Return two database queries for two successive, days, weeks
    months, etc.

    db   :  the database to query
    days :  the number of days each period should be

    """
    last, this = date_spans(days, 2)
    last_start, last_end = last
    this_start, this_end = this
    last_period = data(db, "between", last_start, last_end)
    this_period = data(db, "between", this_start, this_end)
    return (last_period, this_period)


def changing_counts(last_period, this_period):
    """
    Return sorted sequence of words with the greatest 
    frequency changes from one import period to the next.
    
    Separate sequences for rising and falling words.

    """
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
