#!/usr/bin/env python


import datetime as dt

from query_database import query, word_on_date

from constants import TODAY, BBC_DATABASE


def date_factory(num_days):
    return TODAY - dt.timedelta(days=num_days)


def get_word_trends(db, word, days):
    day_nums = [n for n in range(days, -1, -1)]
    dates = [date_factory(n) for n in day_nums]
    counts = []
    for date in dates:
        data = query(db, word_on_date, (date, word))
        for datum in data:
            _, count, _ = datum
            if count:
                counts.append(count)
            else:
                counts.append(0)
    dates = [d.strftime('%d %B') for d in dates]
    return dict(zip(dates, counts))


MAY = get_word_trends(BBC_DATABASE, 'may', 7)
CORBYN = get_word_trends(BBC_DATABASE, 'corbyn', 7)
DEATH = get_word_trends(BBC_DATABASE, 'death', 7)
BBC = get_word_trends(BBC_DATABASE, 'bbc', 7)
ELECTION = get_word_trends(BBC_DATABASE, 'election', 10)
