from constants import GRAPH_PATH
from query import word_count, word_count_period
from query_functions import TODAY, YESTERDAY, date_range, date_spans


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
        self.colour = colour
        self.period = period
        self.path = path

    def plot_data(self):
        if not self.period:
            dates = date_range(YESTERDAY, self.days)
            counts = [word_count(self.db, word, dates) for word in self.words]
            date_labels = [date.strftime('%d %B') for date in dates]
        else:
            date_labels = []
            dates = date_spans(self.days, self.period)
            counts = [word_count_period(self.db, word, dates) for word in self.words]
            for date in dates:
                start, end = date
                date_labels.append(end.strftime('%d %B'))
            # Reset final date label to today
            date_labels[-1] = TODAY.strftime('%d %B')
        return (self.words, date_labels, counts)


def get_plot(title, filename, source=None, path=GRAPH_PATH):
    """ Return graph object for display. """
    return {"title": title,
            "plot": ''.join([path, filename]),
            "source": source}
