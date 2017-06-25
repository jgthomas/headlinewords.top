import random
import functools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from constants import (PLOT_PATH,
                       TABLEAU, COLOURS,
                       RED, BLUE, PINK,
                       GREY, ORANGE, GREEN,
                       LIGHT_GREY)


def pick_colours(colour_list, num):
    """ Return randomly selected colours. """
    colours = []
    opts = colour_list[:]
    for i in range(num):
        choice = random.choice(opts)
        opts.remove(choice)
        colours.append(choice)
    return colours


def plot_style(func):
    """ Shared style for graphs. """
    @functools.wraps(func)
    def style_wrapper(*args, **kwargs):
        params = {'figure.figsize': [16, 12],
                  'legend.frameon': False,
                  'legend.fontsize': 28,
                  'legend.loc': "upper right",
                  'legend.markerscale': 0,
                  'legend.handlelength': 0,
                  'lines.linewidth': 6}
        plt.rcParams.update(params)
        # Remove frame
        ax = plt.subplot(111)
        ax.spines["top"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        # Remove tick marks
        plt.tick_params(bottom="off", left="off")
        func(*args, **kwargs)
    return style_wrapper


@plot_style
def bar_plot(data):
    colour = COLOURS[data["colour"]]
    plt.bar(range(len(data["sources"])),
            data["sources"].values(),
            align="center",
            color=colour)
    plt.xticks(range(len(data["sources"])),
               list(data["sources"].keys()),
               rotation=55,
               fontsize=24,
               ha="right")
    plt.yticks(fontsize=24,
               weight='bold')
    plt.title("'{}'".format(data["word"]),
              fontsize=28)

    plt.subplots_adjust(bottom=0.33)

    outfile = ''.join([data["path"], data["filename"]])
    plt.savefig(outfile)

    plt.clf()


@plot_style
def line_plot(data):
    words, x_data, y_data = data.plot_data()
    filename = data.filename if data.filename else None
    colour = data.colour
    path = data.path if data.path else PLOT_PATH

    plt.yticks(fontsize=24, weight='bold')
    plt.xticks(range(len(x_data)), x_data, rotation=45, fontsize=24)

    # Hide some labels for longer data sets
    if len(x_data) > 14:
        for index, label in enumerate(ax.xaxis.get_ticklabels()):
            if index % 2 == 0:
                label.set_visible(False)

    # Randomly select nice colours if none specified
    if not colour:
        colour = pick_colours(TABLEAU, len(words))

    # Plot data
    for index, word in enumerate(words):
        plt.plot(y_data[index], color=colour[index])

    # Set y-axis to start at zero
    plt.ylim(ymin=0)

    # Add legend, position horizontally above plot
    leg = plt.legend(words, bbox_to_anchor=(1, 1),
                     bbox_transform=plt.gcf().transFigure,
                     ncol=len(words))

    # Match legend line- and text-colours (line is hidden by params)
    for line, text in zip(leg.get_lines(), leg.get_texts()):
        text.set_color(line.get_color())

    plt.subplots_adjust(bottom=0.25)

    # If no name specified, use first word
    if not filename:
        filename, *rest = words
    outfile = ''.join([path, filename])
    plt.savefig(outfile)

    plt.clf()
