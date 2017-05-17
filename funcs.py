

import json
import datetime as dt


def date_object():
    """ Return date object for today with only year, month and day. """
    now = dt.datetime.now()
    today = dt.date(now.year, now.month, now.day)
    return today


def date_factory(start, num_days):
    """ Return a date object for num_days prior to start. """
    return start - dt.timedelta(days=num_days)


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
