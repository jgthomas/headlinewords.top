

import unittest

from process_words import word_filter
from constants import STOPWORDS

class Test(unittest.TestCase):
    def test_lowercase(self):
        words_in = ['DOG', 'Man' 'CaT', "pOny'S", 'Hound-tootHED']
        words_out = ['dog', 'man' 'cat', "pony's", 'hound-toothed']
        with open(STOPWORDS) as swf:
            to_ignore = set(line.strip() for line in swf)
        self.assertListEqual(words_out, list(word_filter(words_in, to_ignore)))

    def test_remove_quotes(self):
        words_in = ["'hourly'", "'heroically'", "'themes''", "'weirdly"]
        words_out = ["hourly", "heroically", "themes'", "weirdly"]
        with open(STOPWORDS) as swf:
            to_ignore = set(line.strip() for line in swf)
        self.assertListEqual(words_out, list(word_filter(words_in, to_ignore)))

    def test_convert_unicode_apostrophe(self):
        """ Keep plural apostrophe while removing trailing quote. """
        words_in = ["\u2018yacht\u2019", "hero\u2019s",
                    "states\u2019", "\u2018grandpas\u2019\u2019",
                    "\u2018nations\u2019\u2019", "warriors'"]
        words_out = ["yacht", "hero's", "states'", "grandpas'",
                     "nations'", "warriors'"]
        with open(STOPWORDS) as swf:
            to_ignore = set(line.strip() for line in swf)
        self.assertListEqual(words_out, list(word_filter(words_in, to_ignore)))

    def test_del_noninitial_nonword_chars(self):
        """ Keep apostrophe and hypen. """
        words_in = ["overmatch", "dogs!", "warne@", "o%wners'", "all)-in"]
        words_out = ["overmatch", "dogs", "warne", "owners'", "all-in"]
        with open(STOPWORDS) as swf:
            to_ignore = set(line.strip() for line in swf)
        self.assertListEqual(words_out, list(word_filter(words_in, to_ignore)))

    def test_remove_stopwords(self):
        """ Watch for stopwords paired with punctuation. """
        words_in = ["however", "asking:", "this", "that", "2ever", "to*day"]
        words_out = []
        with open(STOPWORDS) as swf:
            to_ignore = set(line.strip() for line in swf)
        self.assertListEqual(words_out, list(word_filter(words_in, to_ignore)))


if __name__ == '__main__':
    unittest.main()
