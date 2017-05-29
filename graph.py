

class Graph(object):

    path = 'images/plots/'
    ext = '.png'
    
    def __init__(self, title, db, filename, days, words, colour=None):
        self.title = title
        self.db = db
        self.filename = filename
        self.days = days
        self.words = words
        self.colour = colour if colour else ["random"]

        self.args = ["--words", self.words,
                     "--days", self.days,
                     "--colour", self.colour,
                     "--database", self.db,
                     "--filename", self.filename]

        self.plot = ''.join([self.__class__.path,
                             self.filename, 
                             self.__class__.ext])
