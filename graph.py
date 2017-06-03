

GRAPH_PATH = 'images/plots/'


class Graph(object):

    def __init__(self, db, filename, days, words, colour=None, period=False):
        self.db = db
        self.filename = filename
        self.days = days
        self.words = words
        self.colour = colour if colour else ["random"]
        self.period = period

    def args(self):
        args = ["--words", self.words,
                "--days", self.days,
                "--colour", self.colour,
                "--database", self.db,
                "--filename", self.filename]
        if self.period:
            args.append("--period")
            args.append(self.period)
        return args



def get_plot(title, filename, source=None):
    return {"title": title,
            "plot": ''.join([GRAPH_PATH, filename]),
            "source": source}
