#!/usr/bin/env python


import feedparser


# In use
BBC_URL = 'http://feeds.bbci.co.uk/news/uk/rss.xml'
NYT_URL = 'http://rss.nytimes.com/services/xml/rss/nyt/US.xml'
DML_URL = 'http://www.dailymail.co.uk/home/index.rss'
FOX_URL = 'http://feeds.foxnews.com/foxnews/national?format=xml'
SMH_URL = 'http://www.smh.com.au/rssheadlines/top.xml'
ABC_URL = 'http://www.abc.net.au/news/feed/45910/rss.xml'
SKY_URL = 'http://feeds.skynews.com/feeds/rss/uk.xml'
IND_URL = 'https://www.independent.co.uk/news/uk/rss'

# Candidates
EXP_URL = 'https://feeds.feedburner.com/daily-express-uk-news'
WPO_URL = 'http://feeds.washingtonpost.com/rss/national'
NYP_URL = 'https://nypost.com/news/feed/'
GDN_URL = 'https://www.theguardian.com/uk-news/rss'
TOI_URL = 'http://timesofindia.indiatimes.com/rssfeeds/296589292.cms'
HIT_URL = 'http://www.hindustantimes.com/rss/world/rssfeed.xml'


def get_headlines(url):
    """ Pull down RSS feed and extract the headlines. """
    feed = feedparser.parse(url)
    headlines = [x['title'] for x in feed['entries']]
    return headlines


# Sources
BBC = get_headlines(BBC_URL)
NYT = get_headlines(NYT_URL)
DML = get_headlines(DML_URL)
FOX = get_headlines(FOX_URL)
SMH = get_headlines(SMH_URL)
ABC = get_headlines(ABC_URL)
SKY = get_headlines(SKY_URL)
IND = get_headlines(IND_URL)

TOI = get_headlines(TOI_URL)
HIT = get_headlines(HIT_URL)

# Currently used sources
SOURCES = [('bbc', BBC), ('nyt', NYT),
           ('dml', DML), ('fox', FOX),
           ('smh', SMH), ('abc', ABC),
           ('sky', SKY), ('ind', IND),
           ('toi', TOI), ('hit', HIT)]
