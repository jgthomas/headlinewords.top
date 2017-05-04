

import json
import datetime as dt


def save_to_json(filename, words):
    with open(filename, 'w') as outfile:
        json.dump(words, outfile)


def load_words(words):
    with open(words, 'r') as infile:
        todays_words = json.load(infile)
    return todays_words


def date_object():
    """ Return date object for today with only year, month and day. """
    now = dt.datetime.now()
    today = dt.date(now.year, now.month, now.day)
    return today


def date_object_factory(number_of_days):
    return TODAY - dt.timedelta(days=number_of_days)


def name_factory(date, name):
    date = date.strftime("%d_%m_%Y")
    return '_'.join([date, name])
