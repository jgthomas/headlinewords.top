

import json
import datetime as dt


def load_words(words):
    with open(words, 'r') as infile:
        todays_words = json.load(infile)
    return todays_words


def date_object():
    """ Return date object for today with only year, month and day. """
    now = dt.datetime.now()
    today = dt.date(now.year, now.month, now.day)
    return today
