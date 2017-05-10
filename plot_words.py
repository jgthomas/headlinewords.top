#!/usr/bin/env python


import datetime as dt

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from query_database import query, word_on_date

from constants import TODAY, BBC_DATABASE


GRAPH_PATH = 'graphs/'


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
    return (word, dates, counts)


ELECTION = get_word_trends(BBC_DATABASE, 'election', 30)
AFTER = get_word_trends(BBC_DATABASE, 'after', 7)


def plot_graph(data):
    word, x_data, y_data = data
    plt.rcParams['figure.figsize'] = 12, 8
    plt.plot(y_data)
    plt.xticks(range(len(x_data)), x_data, rotation=45)
    plt.title(word)
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    plt.subplots_adjust(bottom=0.25)
    plt.savefig(''.join([GRAPH_PATH, word, '.png']))
    plt.clf()


def main():
    plot_graph(AFTER)
    plot_graph(ELECTION)

if __name__ == '__main__':

    main()
