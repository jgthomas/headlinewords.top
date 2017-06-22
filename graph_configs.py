import plot_words
from constants import SHORT_N_WORDS
from graph import Graph
from query_functions import just_words
from query import data


# HOMEPAGE
HOMEPAGE_BBC_1 = Graph(db = "bbc",
                       filename = "homepage_bbc_1",
                       days = "7",
                       words = ['manchester', 'london'],
                       colour = ['red', 'blue'],
                       period="4")

HOMEPAGE_NYT_1 = Graph(db = "nyt",
                       filename = "homepage_nyt_1",
                       days = "7",
                       words = just_words(data("nyt", "ever"))[:SHORT_N_WORDS],
                       period = "4")


# BBC
BBC_TODAY_1 = Graph(db = "bbc",
                    filename = "bbc_today_1",
                    days = "7",
                    words = ['conservative', 'labour'],
                    colour = ['blue', 'red'],
                    period = "4")

BBC_TODAY_2 = Graph(db = "bbc",
                    filename = "bbc_today_2",
                    days = "14",
                    words = ['attack', 'bomb', 'threat', 'terror'])

BBC_WEEK_1 = Graph(db = "bbc",
                   filename = 'bbc_week_1',
                   days = "7",
                   words = just_words(data("bbc", "since", "week"))[:SHORT_N_WORDS])

BBC_WEEK_2 = Graph(db = "bbc",
                   filename = 'bbc_week_2',
                   days = "7",
                   words = ['corbyn', 'may'],
                   colour = ['red', 'blue'])

BBC_MONTH_1 = Graph(db = "bbc",
                    filename = 'bbc_month_1',
                    days = "7",
                    words = just_words(data("bbc", "since", "month"))[:SHORT_N_WORDS],
                    period = "4")

BBC_MONTH_2 = Graph(db = "bbc",
                    filename = 'bbc_month_2',
                    days = "7",
                    words = ["death", "dead", "murder", "killed"],
                    period="4")

BBC_EVER_1 = Graph(db = "bbc",
                   filename = "bbc_ever_1",
                   days = "7",
                   words = just_words(data("bbc", "ever"))[:SHORT_N_WORDS],
                   period = "4")

BBC_EVER_2 = Graph(db = "bbc",
                   filename = "bbc_ever_2",
                   days = "7",
                   words = ["london", "manchester", "birmingham", "liverpool", "newcastle"],
                   period = "4")


# NYT
NYT_TODAY_1 = Graph(db = "nyt",
                    filename = 'nyt_today_1',
                    days = "7",
                    words = ['trump', 'ivanka', 'kushner', 'melania'],
                    period = "4")

NYT_TODAY_2 = Graph(db = "nyt",
                    filename = 'nyt_today_2',
                    days = "7",
                    words = ['fbi', 'comey', 'russia', 'investigation'],
                    period = "4")

NYT_WEEK_1 = Graph(db = "nyt",
                   filename = 'nyt_week_1',
                   days = "7",
                   words = just_words(data("nyt", "since", "week"))[:SHORT_N_WORDS])

NYT_MONTH_1 = Graph(db = "nyt",
                    filename = 'nyt_month_1',
                    days = "7",
                    words = just_words(data("nyt", "since", "month"))[:SHORT_N_WORDS],
                    period = "4")

NYT_EVER_1 = Graph(db = "nyt",
                   filename = 'nyt_ever_1',
                   days = "7",
                   words = just_words(data("nyt", "ever"))[:SHORT_N_WORDS],
                   period = "4")


GRAPHS_IN_USE = [HOMEPAGE_BBC_1,
                 HOMEPAGE_NYT_1,
                 BBC_TODAY_1,
                 BBC_TODAY_2,
                 BBC_WEEK_1,
                 BBC_WEEK_2,
                 BBC_MONTH_1,
                 BBC_MONTH_2,
                 BBC_EVER_1,
                 BBC_EVER_2,
                 NYT_TODAY_1,
                 NYT_TODAY_2,
                 NYT_WEEK_1,
                 NYT_MONTH_1,
                 NYT_EVER_1]


def main():
    for graph in GRAPHS_IN_USE:
        plot_words.main(graph.args())


if __name__ == '__main__':
    main()
