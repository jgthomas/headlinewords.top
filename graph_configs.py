

import plot_words
from constants import SHORT_N_WORDS
from graph import Graph
from query_functions import just_words
from query import data


BBC_DB = "bbc"
NYT_DB = "nyt"


### HOMEPAGE ###
HOMEPAGE_BBC_1 = Graph(db = BBC_DB,
                       filename = "homepage_bbc_1",
                       days = "14",
                       words = ['manchester'],
                       colour = ['red'])

HOMEPAGE_NYT_1 = Graph(db = NYT_DB,
                       filename = "homepage_nyt_1",
                       days = "7",
                       words = just_words(data("nyt", "ever"))[:SHORT_N_WORDS],
                       period = "4")


### BBC TODAY ###
BBC_TODAY_1 = Graph(db = BBC_DB,
                    filename = "bbc_today_1",
                    days = "7",
                    words = ['conservative', 'labour'],
                    colour = ['blue', 'red'],
                    period = "4")

BBC_TODAY_2 = Graph(db = BBC_DB,
                    filename = "bbc_today_2",
                    days = "14",
                    words = ['attack', 'bomb', 'threat', 'terror'])


### BBC WEEK ###
BBC_WEEK_1 = Graph(db = BBC_DB,
                   filename = 'bbc_week_1',
                   days = "7",
                   words = just_words(data("bbc", "since", "week"))[:SHORT_N_WORDS])

BBC_WEEK_2 = Graph(db = BBC_DB,
                   filename = 'bbc_week_2',
                   days = "7",
                   words = ['corbyn', 'may'],
                   colour = ['red', 'blue'])


### BBC MONTH ###
BBC_MONTH_1 = Graph(db = BBC_DB,
                    filename = 'bbc_month_1',
                    days = "7",
                    words = just_words(data("bbc", "since", "month"))[:SHORT_N_WORDS],
                    period = "4")

BBC_MONTH_2 = Graph(db = BBC_DB,
                    filename = 'bbc_month_2',
                    days = "30",
                    words = ["death", "dead", "murder", "killed"])


### BBC EVER ###
BBC_EVER_1 = Graph(db = BBC_DB,
                   filename = "bbc_ever_1",
                   days = "7",
                   words = just_words(data("bbc", "ever"))[:SHORT_N_WORDS],
                   period = "4")

BBC_EVER_2 = Graph(db = BBC_DB,
                   filename = "bbc_ever_2",
                   days = "7",
                   words = ["london", "manchester", "birmingham", "liverpool", "newcastle"],
                   period = "4")


### NYT TODAY ###

### NYT WEEK ###
NYT_WEEK_1 = Graph(db = NYT_DB,
                   filename = 'nyt_week_1',
                   days = "7",
                   words = just_words(data("nyt", "since", "week"))[:SHORT_N_WORDS])


### NYT MONTH ###
NYT_MONTH_1 = Graph(db = NYT_DB,
                    filename = 'nyt_month_1',
                    days = "7",
                    words = ['trump', 'ivanka', 'kushner', 'melania'],
                    period = "4")

NYT_MONTH_2 = Graph(db = NYT_DB,
                    filename = 'nyt_month_2',
                    days = "7",
                    words = ['fbi', 'comey', 'russia', 'investigation'],
                    period =  "4")

### NYT EVER ###


def main():
    ## Homepage
    plot_words.main(HOMEPAGE_BBC_1.args())
    plot_words.main(HOMEPAGE_NYT_1.args())
    ## BBC Today
    plot_words.main(BBC_TODAY_1.args())
    plot_words.main(BBC_TODAY_2.args())
    ## BBC Week
    plot_words.main(BBC_WEEK_1.args())
    plot_words.main(BBC_WEEK_2.args())
    ## BBC Month
    plot_words.main(BBC_MONTH_1.args())
    plot_words.main(BBC_MONTH_2.args())
    ## BBC Ever
    plot_words.main(BBC_EVER_1.args())
    plot_words.main(BBC_EVER_2.args())
    ## NYT Week
    plot_words.main(NYT_WEEK_1.args())
    ## NYT Month
    plot_words.main(NYT_MONTH_1.args())
    plot_words.main(NYT_MONTH_2.args())


if __name__ == '__main__':

    main()
