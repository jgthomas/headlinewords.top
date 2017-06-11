

import unittest

from process_words import filter_words

class Test(unittest.TestCase):
    def test_general_stopwords(self):
        source = 'generic'
        words_in = ["other", "this", "that", "the",
                    "news", "headlines", "briefing"]
        words_out = ["news", "headlines", "briefing"]
        self.assertListEqual(words_out, list(filter_words(source, words_in)))

    def test_bbc_stopwords(self):
        source = 'bbc'
        words_in = ["other", "this", "that", "the",
                    "news", "headlines", "briefing"]
        words_out = ["briefing"]
        self.assertListEqual(words_out, list(filter_words(source, words_in)))

    def test_nyt_stopwords(self):
        source = 'nyt'
        words_in = ["other", "this", "that", "the",
                    "news", "headlines", "briefing"]
        words_out = ["news", "headlines"]
        self.assertListEqual(words_out, list(filter_words(source, words_in)))


if __name__ == '__main__':
    unittest.main()
