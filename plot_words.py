#!/usr/bin/env python


import random
import argparse
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from query_database import YESTERDAY, date_object_range, word_counts

from constants import (DATABASES, BBC_DATABASE, NYT_DATABASE,
                       PLOT_PATH,
                       TABLEAU, COLOURS,
                       RED, BLUE, PINK,
                       GREY, ORANGE, GREEN,
                       LIGHT_GREY)


def get_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', type=str)
    parser.add_argument('--database', type=str)
    parser.add_argument('--days', type=int)
    parser.add_argument('--colour', nargs='+')
    parser.add_argument('--words', nargs='+')
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


def get_plot_data(db, wordlist, days):
    dates = date_object_range(YESTERDAY, days)
    counts = [word_counts(db, word, dates) for word in wordlist]
    date_labels = [date.strftime('%d %B') for date in dates]
    return (wordlist, date_labels, counts)


def plot_words(data, *, filename=None, colour=None):
    words, x_data, y_data = data

    # set plot parameters
    params = {'figure.figsize': [16, 12],
              'legend.frameon': False,
              'legend.fontsize': 24,
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

    # add legend, position horizontally above plot
    leg = plt.legend(words, bbox_to_anchor=(0.5, 1), 
                     bbox_transform=plt.gcf().transFigure,
                     ncol=len(words))
    # match legend line and text colours (line is hidden by params)
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


def main(args):
    args = get_args(args)
    words = args.words
    title = args.title if args.title else None
    days = args.days if args.days else 7
    database = DATABASES[args.database] if args.database else BBC_DATABASE
    colour = None
    if args.colour:
        colour = [COLOURS[colour] for colour in args.colour]
    data = get_plot_data(database, words, days)
    plot_words(data, filename=title, colour=colour)


if __name__=='__main__':

    main(sys.argv[1:])
