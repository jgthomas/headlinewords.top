#!/usr/bin/env python


import random
import datetime as dt

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from query_database import query, word_on_date

from constants import (YESTERDAY, 
                       TODAY, 
                       BBC_DATABASE, 
                       PLOT_PATH, 
                       RED, 
                       BLUE,
                       PINK,
                       GREY,
                       ORANGE,
                       GREEN,
                       TABLEAU)


def date_factory(num_days):
    """ Return a date object for num_days prior to present. """
    return YESTERDAY - dt.timedelta(days=num_days)


def date_range(days):
    """ Return a range of consecutive date objects """
    day_nums = [n for n in range(days, -1, -1)]
    return [date_factory(n) for n in day_nums]


def random_colours(colour_list, num):
    """ Return n number of randomly selected colours. """
    colours = []
    opts = colour_list[:]
    for i in range(num):
        choice = random.choice(opts)
        opts.remove(choice)
        colours.append(choice)
    return colours


def get_word_trends(db, word, days):
    dates = date_range(days)
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


def get_many_word_trends(db, wordlist, days):
    dates = date_range(days)
    words = []
    counts = []
    for word in wordlist:
        temp = get_word_trends(db, word, days)
        word, _, count = temp
        words.append(word)
        counts.append(count)
    dates = [d.strftime('%d %B') for d in dates]
    return (words, dates, counts)


#def plot_graph(data):
#    word, x_data, y_data = data
#    plt.rcParams['figure.figsize'] = 12, 8
#    plt.plot(y_data)
#    plt.xticks(range(len(x_data)), x_data, rotation=45)
#    plt.title(word.title())
#    plt.xlabel('Date')
#    plt.ylabel('Frequency')
#    plt.subplots_adjust(bottom=0.25)
#    plt.savefig(''.join([PLOT_PATH, word.title(), '.png']))
#    plt.clf()


def plot_multi(data, *, filename=None, colour=None):
    words, x_data, y_data = data

    # set plot parameters
    params = {'figure.figsize': [16, 12],
              'legend.frameon': False,
              'legend.fontsize': 18,
              'legend.loc': "upper right",
              'legend.markerscale': 0,
              'legend.handlelength': 0,
              'lines.linewidth': 4}
    plt.rcParams.update(params)
    
    # remove the frame
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # remove tick marks
    plt.tick_params(bottom="off", left="off")

    # format the axes and title
    plt.yticks(fontsize=14)
    plt.xticks(range(len(x_data)), x_data, rotation=45, fontsize=14)

    # randomly select nice colours if none specified
    if not colour:
        colour = random_colours(TABLEAU, len(words))

    # plot data
    for index, word in enumerate(words):
        plt.plot(y_data[index], color=colour[index])

    # add legend, and match line and text colours
    leg = plt.legend(words)
    for line, text in zip(leg.get_lines(), leg.get_texts()):
        text.set_color(line.get_color())

    # adjust
    plt.subplots_adjust(bottom=0.25)

    # save: if no name specified, use first word
    if not filename:
        filename, *rest = words
    outfile = ''.join([PLOT_PATH, filename, '.png'])
    plt.savefig(outfile, bbox_inches="tight")

    # close
    plt.clf()


def main():
    WORDZ = ['conservative', 'labour']
    goo = get_many_word_trends(BBC_DATABASE, WORDZ, 7)
    plot_multi(goo, filename='political_parties', colour=(BLUE, RED))

if __name__ == '__main__':

    main()
