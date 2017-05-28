

import plot_words
from query_database import BBC_WEEK, BBC_MONTH, BBC_EVER, NYT_EVER, just_words
from constants import SHORT_N_WORDS


BBC_DB = "bbc"
NYT_DB = "nyt"
GRAPH_PATH = "images/plots/"


### HOMEPAGE ###
# Title and filepath
HOMEPAGE_BBC_TITLE_1 = "We never used to talk about Manchester"
HOMEPAGE_BBC_FILE_1 = "homepage_bbc_1.png"
HOMEPAGE_BBC_PLOT_1 = ''.join([GRAPH_PATH, HOMEPAGE_BBC_FILE_1])

HOMEPAGE_NYT_TITLE_1 = "All Trump, all the time"
HOMEPAGE_NYT_FILE_1 = "homepage_nyt_1.png"
HOMEPAGE_NYT_PLOT_1 = ''.join([GRAPH_PATH, HOMEPAGE_NYT_FILE_1])

# Parameters
HOMEPAGE_BBC_WORDS_1 = ["manchester"]
HOMEPAGE_BBC_DAYS_1 = "14"
HOMEPAGE_BBC_COLOUR_1 = ["red"]
HOMEPAGE_BBC_FILENAME_1 = "homepage_bbc_1"

HOMEPAGE_NYT_WORDS_1 = just_words(NYT_EVER)[:SHORT_N_WORDS]
HOMEPAGE_NYT_DAYS_1 = "14"
HOMEPAGE_NYT_COLOUR_1 = ["random"]
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


### BBC TODAY ###
# Title and filepath
BBC_TODAY_TITLE_1 = "Talking about the parties"
BBC_TODAY_FILE_1 = "bbc_today_1.png"
BBC_TODAY_PLOT_1 = ''.join([GRAPH_PATH, BBC_TODAY_FILE_1])

BBC_TODAY_TITLE_2 = "Danger!"
BBC_TODAY_FILE_2 = "bbc_today_2.png"
BBC_TODAY_PLOT_2 = ''.join([GRAPH_PATH, BBC_TODAY_FILE_2])

# Parameters
BBC_TODAY_WORDS_1 = ["conservative", "labour"]
BBC_TODAY_DAYS_1 = "14"
BBC_TODAY_COLOUR_1 = ["blue", "red"]
BBC_TODAY_FILENAME_1 = "bbc_today_1"

BBC_TODAY_WORDS_2 = ["attack", "bomb", "threat", "terror"]
BBC_TODAY_DAYS_2 = "14"
BBC_TODAY_COLOUR_2 = ["random"]
BBC_TODAY_FILENAME_2 = "bbc_today_2"

# Command line arguments
BBC_TODAY_1 = ["--words", BBC_TODAY_WORDS_1,
               "--days", BBC_TODAY_DAYS_1,
               "--colour", BBC_TODAY_COLOUR_1,
               "--database", BBC_DB,
               "--filename", BBC_TODAY_FILENAME_1]

BBC_TODAY_2 = ["--words", BBC_TODAY_WORDS_2,
               "--days", BBC_TODAY_DAYS_2,
               "--colour", BBC_TODAY_COLOUR_2,
               "--database", BBC_DB,
               "--filename", BBC_TODAY_FILENAME_2]


### BBC WEEK ###
# Title and filepath
BBC_WEEK_TITLE_1 = "Top five this week"
BBC_WEEK_FILE_1 = "bbc_week_1.png"
BBC_WEEK_PLOT_1 = ''.join([GRAPH_PATH, BBC_WEEK_FILE_1])

BBC_WEEK_TITLE_2 = "Follow the leader"
BBC_WEEK_FILE_2 = "bbc_week_2.png"
BBC_WEEK_PLOT_2 = ''.join([GRAPH_PATH, BBC_WEEK_FILE_2])

# Parameters
BBC_WEEK_WORDS_1 = just_words(BBC_WEEK)[:SHORT_N_WORDS]
BBC_WEEK_DAYS_1 = "7"
BBC_WEEK_COLOUR_1 = ["random"]
BBC_WEEK_FILENAME_1 = "bbc_week_1"

BBC_WEEK_WORDS_2 = ["corbyn", "may"]
BBC_WEEK_DAYS_2 = "7"
BBC_WEEK_COLOUR_2 = ["red", "blue"]
BBC_WEEK_FILENAME_2 = "bbc_week_2"

# Command line arguments
BBC_WEEK_1 = ["--words", BBC_WEEK_WORDS_1,
              "--days", BBC_WEEK_DAYS_1,
              "--colour", BBC_WEEK_COLOUR_1,
              "--database", BBC_DB,
              "--filename", BBC_WEEK_FILENAME_1]

BBC_WEEK_2 = ["--words", BBC_WEEK_WORDS_2,
              "--days", BBC_WEEK_DAYS_2,
              "--colour", BBC_WEEK_COLOUR_2,
              "--database", BBC_DB,
              "--filename", BBC_WEEK_FILENAME_2]


### BBC MONTH ###
# Title and filepath
BBC_MONTH_TITLE_1 = "Top five this month"
BBC_MONTH_FILE_1 = "bbc_month_1.png"
BBC_MONTH_PLOT_1 = ''.join([GRAPH_PATH, BBC_MONTH_FILE_1])

BBC_MONTH_TITLE_2 = "The grimmest reaper"
BBC_MONTH_FILE_2 = "bbc_month_2.png"
BBC_MONTH_PLOT_2 = ''.join([GRAPH_PATH, BBC_MONTH_FILE_2])

# Parameters
BBC_MONTH_WORDS_1 = just_words(BBC_MONTH)[:SHORT_N_WORDS]
BBC_MONTH_DAYS_1 = "30"
BBC_MONTH_COLOUR_1 = ["random"]
BBC_MONTH_FILENAME_1 = "bbc_month_1"

BBC_MONTH_WORDS_2 = ["death", "dead", "murder", "killed"]
BBC_MONTH_DAYS_2 = "30"
BBC_MONTH_COLOUR_2 = ["random"]
BBC_MONTH_FILENAME_2 = "bbc_month_2"

# Command line arguments
BBC_MONTH_1 = ["--words", BBC_MONTH_WORDS_1,
               "--days", BBC_MONTH_DAYS_1,
               "--colour", BBC_MONTH_COLOUR_1,
               "--database", BBC_DB,
               "--filename", BBC_MONTH_FILENAME_1]

BBC_MONTH_2 = ["--words", BBC_MONTH_WORDS_2,
               "--days", BBC_MONTH_DAYS_2,
               "--colour", BBC_MONTH_COLOUR_2,
               "--database", BBC_DB,
               "--filename", BBC_MONTH_FILENAME_2]


### BBC Ever ###
# Title and filepath
BBC_EVER_TITLE_1 = "Top five since this all started"
BBC_EVER_FILE_1 = "bbc_ever_1.png"
BBC_EVER_PLOT_1 = ''.join([GRAPH_PATH, BBC_EVER_FILE_1])

BBC_EVER_TITLE_2 = "City limits"
BBC_EVER_FILE_2 = "bbc_ever_2.png"
BBC_EVER_PLOT_2 = ''.join([GRAPH_PATH, BBC_EVER_FILE_2])

# Parameters
BBC_EVER_WORDS_1 = just_words(BBC_EVER)[:SHORT_N_WORDS]
BBC_EVER_DAYS_1 = "30"
BBC_EVER_COLOUR_1 = ["random"]
BBC_EVER_FILENAME_1 = "bbc_ever_1"

BBC_EVER_WORDS_2 = ["london", "manchester", "birmingham", "liverpool", "newcastle"]
BBC_EVER_DAYS_2 = "30"
BBC_EVER_COLOUR_2 = ["random"]
BBC_EVER_FILENAME_2 = "bbc_ever_2"

# Command line arguments
BBC_EVER_1 = ["--words", BBC_EVER_WORDS_1,
               "--days", BBC_EVER_DAYS_1,
               "--colour", BBC_EVER_COLOUR_1,
               "--database", BBC_DB,
               "--filename", BBC_EVER_FILENAME_1]

BBC_EVER_2 = ["--words", BBC_EVER_WORDS_2,
               "--days", BBC_EVER_DAYS_2,
               "--colour", BBC_EVER_COLOUR_2,
               "--database", BBC_DB,
               "--filename", BBC_EVER_FILENAME_2]


### NYT Today ###
# Title and filepath
# Parameters
# Command line arguments

### NYT Week ###
# Title and filepath
# Parameters
# Command line arguments

### NYT Month ###
# Title and filepath
# Parameters
# Command line arguments

### NYT Ever ###
# Title and filepath
# Parameters
# Command line arguments


def main():
    # Homepage
    plot_words.main(HOMEPAGE_BBC_1)
    plot_words.main(HOMEPAGE_NYT_1)
    # BBC Today
    plot_words.main(BBC_TODAY_1)
    plot_words.main(BBC_TODAY_2)
    # BBC Week
    plot_words.main(BBC_WEEK_1)
    plot_words.main(BBC_WEEK_2)
    # BBC Month
    plot_words.main(BBC_MONTH_1)
    plot_words.main(BBC_MONTH_2)
    # BBC Ever
    plot_words.main(BBC_EVER_1)
    plot_words.main(BBC_EVER_2)


if __name__ == '__main__':

    main()
