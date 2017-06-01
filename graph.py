

class Graph(object):

    path = 'images/plots/'
    ext = '.png'
    
    def __init__(self, title, db, filename, days, words, colour=None, source=None, period=False):
        self.title = title
        self.db = db
        self.filename = filename
        self.days = days
        self.words = words
        self.colour = colour if colour else ["random"]
        self.source = source if source else ''
        self.period = period

        self.plot = ''.join([self.__class__.path,
                             self.filename, 
                             self.__class__.ext])

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
