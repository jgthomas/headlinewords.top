

import plot_words
from query_database import NYT_EVER, just_words
from constants import SHORT_N_WORDS

BBC_DB = "bbc"
NYT_DB = "nyt"


### HOMEPAGE ###

# Titles and images #
HOMEPAGE_BBC_TITLE_1 = "We never used to talk about Manchester"
HOMEPAGE_BBC_PLOT_1 = "images/plots/homepage_bbc_1.png"
HOMEPAGE_NYT_TITLE_1 = "All Trump, all the time"
HOMEPAGE_NYT_PLOT_1 = "images/plots/homepage_nyt_1.png"

# Parameters
HOMEPAGE_BBC_WORDS_1 = ["manchester"]
HOMEPAGE_BBC_DAYS_1 = "14"
HOMEPAGE_BBC_COLOUR_1 = "red"
HOMEPAGE_BBC_FILENAME_1 = "homepage_bbc_1"

HOMEPAGE_NYT_WORDS_1 = just_words(NYT_EVER)[:SHORT_N_WORDS]
HOMEPAGE_NYT_DAYS_1 = "14"
HOMEPAGE_NYT_COLOUR_1 = "random"
HOMEPAGE_NYT_FILENAME_1 = "homepage_nyt_1"

# Command line arguments
HOMEPAGE_BBC_1 = ["--words", HOMEPAGE_BBC_WORDS_1,
                  "--days", HOMEPAGE_BBC_DAYS_1,
                  "--colour", HOMEPAGE_BBC_COLOUR_1,
                  "--database", BBC_DB,
                  "--filename", HOMEPAGE_BBC_FILENAME_1]

HOMEPAGE_NYT_1 = ["--words", HOMEPAGE_NYT_WORDS_1,
                  "--days", HOMEPAGE_NYT_DAYS_1,
                  "--colour", HOMEPAGE_NYT_COLOUR_1,
                  "--database", NYT_DB,
                  "--filename", HOMEPAGE_NYT_FILENAME_1]


def main():
    # Homepage
    plot_words.main(HOMEPAGE_BBC_1)
    plot_words.main(HOMEPAGE_NYT_1)


if __name__ == '__main__':

    main()
