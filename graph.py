from constants import GRAPH_PATH


class Graph(object):

    """
    db        :  database to query
    filename  :  name of output file
    days      :  number of individual days to plot, OR
                 if 'period' is set, the number of days in
                 each period
    words     :  words to plot, either specified directly
                 or pulled from a query
    colour    :  colour to use for each word, if not passed
                 random colours are used
    period    :  number of successive, x periods, of y days,
                 to plot. e.g. days=7 periods=4 is 4 periods of
                 7 days, or 4 weeks
    path      :  location to save the resulting image file

    """

    def __init__(self, db, filename, days, words, colour=None, period=False, path=None):
        self.db = db
        self.filename = filename
        self.days = days
        self.words = words
        self.colour = colour if colour else ["random"]
        self.period = period
        self.path = path

    def args(self):
        """ Command line parameters passed to plot_words module. """
        args = ["--words", self.words,
                "--days", self.days,
                "--colour", self.colour,
                "--database", self.db,
                "--filename", self.filename]
        if self.period:
            args.append("--period")
            args.append(self.period)
        if self.path:
            args.append("--path")
            args.append(self.path)
        return args


def get_plot(title, filename, source=None, path=GRAPH_PATH):
    """ Return graph object for display. """
    return {"title": title,
            "plot": ''.join([path, filename]),
            "source": source}
