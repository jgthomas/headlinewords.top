

import plot_words
from query_database import NYT_EVER, just_words
from constants import SHORT_N_WORDS


## Database name ##
BBC_DB = "bbc"
NYT_DB = "nyt"

## Plot titles and images to load ##
BBC_PLOT_1 = "images/plots/manchester.png"
BBC_TITLE_1 = "We never used to talk about Manchester"
NYT_PLOT_1 = "images/plots/trump.png"
NYT_TITLE_1 = "All Trump, all the time"

## Plots for homepage ##
BBC_PLOT_WORDS_1 = ["manchester"]
BBC_PLOT_DAYS_1 = "14"
BBC_PLOT_COLOUR_1 = "red"
BBC_PLOT_FILENAME_1 = "bbc_homepage_plot_1.png"

NYT_PLOT_WORDS_1 = just_words(NYT_EVER)[:SHORT_N_WORDS]
NYT_PLOT_DAYS_1 = "14"
NYT_PLOT_COLOUR_1 = "random"
NYT_PLOT_FILENAME_1 = "nyt_homepage_plot_1.png"

BBC_HOMEPAGE_PLOT_1 = ["--words", BBC_PLOT_WORDS_1,
                       "--days", BBC_PLOT_DAYS_1,
                       "--colour", BBC_PLOT_COLOUR_1,
                       "--database", BBC_DB]

NYT_HOMEPAGE_PLOT_1 = ["--words", NYT_PLOT_WORDS_1,
                       "--days", NYT_PLOT_DAYS_1,
                       "--colour", NYT_PLOT_COLOUR_1,
                       "--database", NYT_DB]


def main():
    plot_words.main(BBC_HOMEPAGE_PLOT_1)
    plot_words.main(NYT_HOMEPAGE_PLOT_1)


if __name__ == '__main__':

    main()
