

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
