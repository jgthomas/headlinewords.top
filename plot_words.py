#!/usr/bin/env python


import random
import argparse
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from query import word_count, word_count_period

from query_functions import TODAY, YESTERDAY, date_range, date_spans

from constants import (DATABASES, DEFAULT_DATABASE,
                       PLOT_PATH, DEFAULT_PLOT_DAYS,
                       TABLEAU, COLOURS,
                       RED, BLUE, PINK,
                       GREY, ORANGE, GREEN,
                       LIGHT_GREY)


def get_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str)
    parser.add_argument('--database', type=str)
    parser.add_argument('--days', type=int)
    parser.add_argument('--colour', nargs='+')
    parser.add_argument('--words', nargs='+')
    parser.add_argument('--period', nargs='?', const=0, type=int)
    return parser.parse_args(args)


def pick_colours(colour_list, num):
    """ Return randomly selected colours. """
    colours = []
    opts = colour_list[:]
    for i in range(num):
        choice = random.choice(opts)
        opts.remove(choice)
        colours.append(choice)
    return colours


def get_plot_data(db, wordlist, days, period):
    """
    Return sequence of values to plot for each word in _wordlist_.

    db       :  database to query
    wordlist :  words to query
    days     :  number of days to query for each word, OR,
                if period is greater than 0, the number of days
                in each successive period, i.e. 7 in a week
    period   :  defaults to 0, if another number passed, the query
                switches to word counts for _period_ number sequences
                of _days_ days

    Example: Get the word counts for a list of words for each of the
             last ten days, from the BBC.
    >>> get_plot_data('bbc', [wordlist], 10, period=0)

    Example: Get word counts for a list of words, summed for
             the last four weeks, from the BBC.
    >>> get_plot_data('bbc', [wordlist], 7, period=4)

    In each case, a sequence of numbers is returned for each word
    in _wordlist_, which is then used to plot that word on a graph.

    """
    if not period:
        dates = date_range(YESTERDAY, days)
        counts = [word_count(db, word, dates) for word in wordlist]
        date_labels = [date.strftime('%d %B') for date in dates]
    else:
        date_labels = []
        dates = date_spans(days, period)
        counts = [word_count_period(db, word, dates) for word in wordlist]
        for date in dates:
            start, end = date
            date_labels.append(end.strftime('%d %B'))
        # Reset final date label to today
        date_labels[-1] = TODAY.strftime('%d %B')
    return (wordlist, date_labels, counts)


def plot_words(data, *, filename=None, colour=None):
    words, x_data, y_data = data

    # set plot parameters
    params = {'figure.figsize': [16, 12],
              'legend.frameon': False,
              'legend.fontsize': 28,
              'legend.loc': "upper right",
              'legend.markerscale': 0,
              'legend.handlelength': 0,
              'lines.linewidth': 6}
    plt.rcParams.update(params)
    
    # remove the frame
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # remove tick marks
    plt.tick_params(bottom="off", left="off")

    # format the axes
    plt.yticks(fontsize=24, weight='bold')
    plt.xticks(range(len(x_data)), x_data, rotation=45, fontsize=24)

    # Hide some labels for longer data sets
    if len(x_data) > 14:
        for index, label in enumerate(ax.xaxis.get_ticklabels()):
            if index % 2 == 0:
                label.set_visible(False)

    # randomly select nice colours if none specified
    if not colour:
        colour = pick_colours(TABLEAU, len(words))

    # plot data
    for index, word in enumerate(words):
        plt.plot(y_data[index], color=colour[index])

    # set y-axis to start at zero
    plt.ylim(ymin=0)

    # add legend, position horizontally above plot
    leg = plt.legend(words, bbox_to_anchor=(1, 1),
                     bbox_transform=plt.gcf().transFigure,
                     ncol=len(words))
    # match legend line- and text-colours (line is hidden by params)
    for line, text in zip(leg.get_lines(), leg.get_texts()):
        text.set_color(line.get_color())

    # adjust
    plt.subplots_adjust(bottom=0.25)

    # save: if no name specified, use first word
    if not filename:
        filename, *rest = words
    outfile = ''.join([PLOT_PATH, filename, '.png'])
    plt.savefig(outfile)

    # close
    plt.clf()


def main(args):
    args = get_args(args)
    words, *_ = args.words
    #words = args.words
    filename = args.filename if args.filename else None
    days = args.days if args.days else DEFAULT_PLOT_DAYS
    database = args.database
    period = args.period
    colour, *_ = args.colour if args.colour else None
    #colour = args.colour if args.colour else None
    if "random" in colour:
        colour = None
    else:
        colour = [COLOURS[col] for col in colour]
    data = get_plot_data(database, words, days, period)
    plot_words(data, filename=filename, colour=colour)


if __name__=='__main__':

    main(sys.argv[1:])
