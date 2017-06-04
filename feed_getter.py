#!/usr/bin/env python


import feedparser


BBC_URL = 'http://feeds.bbci.co.uk/news/uk/rss.xml'
NYT_URL = 'http://rss.nytimes.com/services/xml/rss/nyt/US.xml'
GDN_URL = 'https://www.theguardian.com/uk-news/rss'
DML_URL = 'http://www.dailymail.co.uk/home/index.rss'
FOX_URL = 'http://feeds.foxnews.com/foxnews/national?format=xml'
SKY_URL = 'http://feeds.skynews.com/feeds/rss/uk.xml'
NYP_URL = 'https://nypost.com/news/feed/'
IND_URL = 'https://www.independent.co.uk/news/uk/rss'
EXP_URL = 'https://feeds.feedburner.com/daily-express-uk-news'
ABC_URL = 'http://feeds.abcnews.com/abcnews/topstories'


def get_headlines(url):
    """ Pull down RSS feed and extract the headlines. """
    feed = feedparser.parse(url)
    headlines = [x['title'] for x in feed['entries']]
    return headlines


# Sources
BBC = get_headlines(BBC_URL)
NYT = get_headlines(NYT_URL)
GDN = get_headlines(GDN_URL)
DML = get_headlines(DML_URL)
FOX = get_headlines(FOX_URL)
SKY = get_headlines(SKY_URL)
NYP = get_headlines(NYP_URL)
IND = get_headlines(IND_URL)
EXP = get_headlines(EXP_URL)

# Currently used sources
SOURCES = [('bbc', BBC), ('nyt', NYT), ('dml', DML), ('fox', FOX)]
