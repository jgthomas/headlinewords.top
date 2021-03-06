# WORDS

# Words to exclude from the database
STOPWORDS = 'static/wordlists/stopwords.txt'
BBC_STOPWORDS = 'static/wordlists/bbc_stopwords.txt'
NYT_STOPWORDS = 'static/wordlists/nyt_stopwords.txt'
FOX_STOPWORDS = 'static/wordlists/fox_stopwords.txt'

# Exclude words shorter than
SHORT_WORD = 2

# Retrieve this many words for queries
SHORT_N_WORDS = 5
TOP_N_WORDS = 10
DOUBLE_N_WORDS = 20
MID_N_WORDS = 50
HIGH_N_WORDS = 200
MAX_N_WORDS = 500


# SOURCES
SOURCES = ["bbc", "nyt", "dml",
           "fox", "smh", "abc",
           "sky", "ind", "toi",
           "hit"]

UK_SOURCES = ['bbc', 'dml', "sky", "ind"]
US_SOURCES = ['nyt', 'fox']
AU_SOURCES = ['smh', 'abc']
IN_SOURCES = ['toi', 'hit']

COUNTRY_SOURCES = {"all": SOURCES, "all_uk": UK_SOURCES,
                   "all_us": US_SOURCES, "all_au": AU_SOURCES,
                   "all_in": IN_SOURCES}

# Databases for each source
BBC_DATABASE = 'data/bbc_headline_words.db'
NYT_DATABASE = 'data/nyt_headline_words.db'
DML_DATABASE = 'data/dml_headline_words.db'
FOX_DATABASE = 'data/fox_headline_words.db'
SMH_DATABASE = 'data/smh_headline_words.db'
ABC_DATABASE = 'data/abc_headline_words.db'
SKY_DATABASE = 'data/sky_headline_words.db'
IND_DATABASE = 'data/ind_headline_words.db'

TOI_DATABASE = 'data/toi_headline_words.db'
HIT_DATABASE = 'data/hit_headline_words.db'

# Database dictionary
DATABASES = {'bbc': BBC_DATABASE, 'nyt': NYT_DATABASE,
             'dml': DML_DATABASE, 'fox': FOX_DATABASE,
             'smh': SMH_DATABASE, 'abc': ABC_DATABASE,
             'sky': SKY_DATABASE, 'ind': IND_DATABASE,
             'toi': TOI_DATABASE, 'hit': HIT_DATABASE}

# Base data for queries
BBC_BASE = {"source": "bbc", "title": "BBC"}
NYT_BASE = {"source": "nyt", "title": "New York Times"}
DML_BASE = {"source": "dml", "title": "Daily Mail"}
FOX_BASE = {"source": "fox", "title": "Fox News"}
SMH_BASE = {"source": "smh", "title": "Sydney Morning Herald"}
ABC_BASE = {"source": "abc", "title": "ABC Australia"}
SKY_BASE = {"source": "sky", "title": "SKY News"}
IND_BASE = {"source": "ind", "title": "The Independent"}

TOI_BASE = {"source": "toi", "title": "Times of India"}
HIT_BASE = {"source": "hit", "title": "Hindustan Times"}

SOURCE_BASE = {"bbc": BBC_BASE, "nyt": NYT_BASE,
               "dml": DML_BASE, "fox": FOX_BASE,
               "smh": SMH_BASE, "abc": ABC_BASE,
               "sky": SKY_BASE, "ind": IND_BASE,
               "toi": TOI_BASE, "hit": HIT_BASE}

UK_BASE = {"source": "uk", "title": "UK"}
US_BASE = {"source": "us", "title": "USA"}
AU_BASE = {"source": "au", "title": "Australia"}
IN_BASE = {"source": "inn", "title": "India"}


# GRAPHS

# Number of days to plot if not specified
DEFAULT_PLOT_DAYS = 7

# To store graphs
PLOT_PATH = 'static/images/plots/'
GRAPH_PATH = 'images/plots/'
ON_DEMAND_PATH = "static/images/plots/ondemand/"
ON_DEMAND_LOAD = "images/plots/ondemand/"

# Some nice plot colours: [0, 1] scaled RGB
BLUE = (0.12156862745098039, 0.4666666666666667, 0.7058823529411765)
RED = (0.8392156862745098, 0.15294117647058825, 0.1568627450980392)
GREEN = (0.17254901960784313, 0.6274509803921569, 0.17254901960784313)
GREY = (0.4980392156862745, 0.4980392156862745, 0.4980392156862745) 
ORANGE = (1.0, 0.4980392156862745, 0.054901960784313725)
PINK = (0.8901960784313725, 0.4666666666666667, 0.7607843137254902) 

# Understated axes colour
LIGHT_GREY = (0.7803921568627451, 0.7803921568627451, 0.7803921568627451)

# Set of nice colors for random selection
TABLEAU = [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765),
           (1.0, 0.4980392156862745, 0.054901960784313725),
           (0.17254901960784313, 0.6274509803921569, 0.17254901960784313),
           (0.8392156862745098, 0.15294117647058825, 0.1568627450980392),
           (0.5803921568627451, 0.403921568627451, 0.7411764705882353),
           (0.5490196078431373, 0.33725490196078434, 0.29411764705882354),
           (0.8901960784313725, 0.4666666666666667, 0.7607843137254902),
           (0.4980392156862745, 0.4980392156862745, 0.4980392156862745),
           (0.7372549019607844, 0.7411764705882353, 0.13333333333333333),
           (0.09019607843137255, 0.7450980392156863, 0.8117647058823529),]

# Colour dictionary
COLOURS =  {'blue': BLUE, 'red': RED, 'green': GREEN, 'grey': GREY,
            'orange': ORANGE, 'pink': PINK}
