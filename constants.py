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

# Databases for each source
BBC_DATABASE = 'data/bbc_headline_words.db'
NYT_DATABASE = 'data/nyt_headline_words.db'
DML_DATABASE = 'data/dml_headline_words.db'
FOX_DATABASE = 'data/fox_headline_words.db'
SMH_DATABASE = 'data/smh_headline_words.db'
ABC_DATABASE = 'data/abc_headline_words.db'

# Database to use if not specified
DEFAULT_DATABASE = BBC_DATABASE

# Database dictionary
DATABASES = {'bbc': BBC_DATABASE, 'nyt': NYT_DATABASE,
             'dml': DML_DATABASE, 'fox': FOX_DATABASE,
             'smh': SMH_DATABASE, 'abc': ABC_DATABASE}

# Base data for queries
BBC_BASE = {"source": "bbc", "title": "BBC"}
NYT_BASE = {"source": "nyt", "title": "New York Times"}
DML_BASE = {"source": "dml", "title": "Daily Mail"}
FOX_BASE = {"source": "fox", "title": "Fox News"}
SMH_BASE = {"source": "smh", "title": "Sydney Morning Herald"}
ABC_BASE = {"source": "abc", "title": "ABC Australia"}
UK_BASE = {"title": "UK"}
US_BASE = {"title": "USA"}
AU_BASE = {"title": "Australia"}

# Number of days to plot if not specified
DEFAULT_PLOT_DAYS = 7

# To store graphs
PLOT_PATH = 'static/images/plots/'

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
