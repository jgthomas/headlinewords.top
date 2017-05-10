

import json
import datetime as dt


def save_to_json(filename, words):
    """ Save data to JSON file. """
    with open(filename, 'w') as outfile:
        json.dump(words, outfile)


def load_words(words):
    """ Get data from JSON file. """
    with open(words, 'r') as infile:
        todays_words = json.load(infile)
    return todays_words


def date_object():
    """ Return date object for today with only year, month and day. """
    now = dt.datetime.now()
    today = dt.date(now.year, now.month, now.day)
    return today


def date_object_factory(number_of_days):
    """ Return date object number_of_days before today. """
    return TODAY - dt.timedelta(days=number_of_days)
