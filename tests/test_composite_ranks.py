

import unittest

from composite_counts import composite_ranks

class Test(unittest.TestCase):
    def test_general_stopwords(self):
        words_in_1 = [["donkey", 10], ["monkey", 2], ["fool", 13]]
        words_in_2 = [["donkey", 10], ["ape", 4], ["fool", 1]]
        words_out = [("donkey", 20), ("fool", 14), ("ape", 4), ("monkey", 2)]
        self.assertListEqual(words_out, composite_ranks([words_in_1, words_in_2]))


if __name__ == '__main__':

    unittest.main()
