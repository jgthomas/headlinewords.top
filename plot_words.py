#!/usr/bin/env python


import random
import datetime as dt

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from query_database import query, word_on_date, YESTERDAY

from funcs import date_factory

from constants import (BBC_DATABASE, 
                       PLOT_PATH, 
                       RED, 
                       BLUE,
                       PINK,
                       GREY,
                       ORANGE,
                       GREEN,
                       LIGHT_GREY,
                       TABLEAU)


def date_range(start, days):
    """ Return a range of consecutive date objects. """
    day_nums = [n for n in range(days, -1, -1)]
    return [date_factory(start, n) for n in day_nums]


def pick_colours(colour_list, num):
    """ Return randomly selected colours. """
    colours = []
    opts = colour_list[:]
    for i in range(num):
        choice = random.choice(opts)
        opts.remove(choice)
        colours.append(choice)
    return colours


def word_counts(db, word, dates):
    """ Return the number of times a word was used on each date. """
    counts = []
    for date in dates:
        for _, count, _ in query(db, word_on_date, (date, word)):
            if count:
                counts.append(count)
            else:
                counts.append(0)
    return counts


def get_trends(db, wordlist, days):
    dates = date_range(YESTERDAY, days)
    counts = [word_counts(db, word, dates) for word in wordlist]
    date_labels = [date.strftime('%d %B') for date in dates]
    return (wordlist, date_labels, counts)


def plot_words(data, *, filename=None, colour=None):
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
    plt.yticks(fontsize=14, color=LIGHT_GREY, weight='bold')
    plt.xticks(range(len(x_data)), x_data, rotation=45, fontsize=14)

    # randomly select nice colours if none specified
    if not colour:
        colour = pick_colours(TABLEAU, len(words))

    # plot data
    for index, word in enumerate(words):
        plt.plot(y_data[index], color=colour[index])

    # set y-axis to start at zero
    plt.ylim(ymin=0)

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
    words1 = ('conservative', 'labour')
    words2 = ('manifesto', 'election')
    w1 = get_trends(BBC_DATABASE, words1, 7)
    w2 = get_trends(BBC_DATABASE, words2, 7)
    plot_words(w1, filename='main_parties', colour=(BLUE, RED))
    plot_words(w2)

if __name__ == '__main__':

    main()
