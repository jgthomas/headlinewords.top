#!/usr/bin/env python


import feedparser


BBC_URL = 'http://feeds.bbci.co.uk/news/uk/rss.xml'


def get_bbc_headlines():
    """ Get BBC News RSS feed and returns all the headlines. """
    feed = feedparser.parse(BBC_URL)
    headlines = [x['title'] for x in feed['entries']]
    return headlines


BBC = get_bbc_headlines()

SOURCES = [BBC]
