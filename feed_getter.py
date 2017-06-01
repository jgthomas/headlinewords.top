#!/usr/bin/env python


import feedparser


BBC_URL = 'http://feeds.bbci.co.uk/news/uk/rss.xml'
NYT_URL = 'http://rss.nytimes.com/services/xml/rss/nyt/US.xml'
GDN_URL = 'https://www.theguardian.com/uk-news/rss'
DML_URL = 'http://www.dailymail.co.uk/home/index.rss'
FOX_URL = 'http://feeds.foxnews.com/foxnews/national?format=xml'


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

# Currently used sources
SOURCES = [('bbc', BBC), ('nyt', NYT), ('dml', DML), ('fox', FOX)]
