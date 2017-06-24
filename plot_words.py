import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from constants import (DATABASES,
                       PLOT_PATH,
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


def bar_plot(sources, filename, colour="blue", path=PLOT_PATH):
    # Set parameters
    params = {'figure.figsize': [16, 12]}
    plt.rcParams.update(params)

    # Remove frame
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Remove tick marks
    plt.tick_params(bottom="off", left="off")

    # Set plot colour
    colour = COLOURS[colour]

    # Plot graph and axes
    plt.bar(range(len(sources["data"])),
            sources["data"].values(),
            align="center",
            color=colour)
    plt.xticks(range(len(sources["data"])),
               list(sources["data"].keys()),
               rotation=55,
               fontsize=24,
               ha="right")
    plt.yticks(fontsize=24, weight='bold')
    plt.title("'{}'".format(sources["word"]),
              fontsize=28)

    # Adjust
    plt.subplots_adjust(bottom=0.33)

    # Save
    outfile = ''.join([path, filename])
    plt.savefig(outfile)

    # Close
    plt.clf()


def line_plot(data):
    words, x_data, y_data = data.plot_data()
    filename = data.filename if data.filename else None
    colour = data.colour
    path = data.path if data.path else PLOT_PATH

    # Set parameters
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

    # Format the axes
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

    # Adjust
    plt.subplots_adjust(bottom=0.25)

    # Save: if no name specified, use first word
    if not filename:
        filename, *rest = words
    outfile = ''.join([path, filename])
    plt.savefig(outfile)

    # Close
    plt.clf()
