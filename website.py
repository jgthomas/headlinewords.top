#!/usr/bin/env python


from flask import Flask, render_template
from flask_ask import Ask, statement, question

from query_database import (BBC_TOP, BBC_TODAY, BBC_WEEK, BBC_MONTH, BBC_EVER,
                            NYT_TOP, NYT_TODAY, NYT_WEEK, NYT_MONTH, NYT_EVER,
                            just_words)


app = Flask(__name__)
ask = Ask(app, "/alexa_skill")


### Alexa ###
@ask.launch
def start_skill():
    welcome_message = "Pick a news source"
    return question(welcome_message)

@ask.intent('BbcIntent')
def read_top_bbc_words():
    words = just_words(BBC_TOP)
    words_message = "The top five from the BBC {}".format(words)
    return statement(words_message) \
           .simple_card(title="Top BBC Words", content=' '.join(words))

@ask.intent('NytIntent')
def read_top_nyt_words():
    words = just_words(NYT_TOP)
    words_message = "The top five from the New York Times {}".format(words)
    return statement(words_message) \
           .simple_card(title="Top NYT Words", content=' '.join(words))


### Homepage ###
@app.route('/')
def home():
    bbc_words = BBC_TOP
    nyt_words = NYT_TOP
    title = 'BBC - Top words today'
    return render_template('index.html', title=title, bbc_words=bbc_words, nyt_words=nyt_words)


### BBC pages ###
@app.route('/bbc/today')
def bbc_today():
    bbc_words = BBC_TODAY
    title = 'BBC - Top words today'
    return render_template('bbc.html', title=title, bbc_words=bbc_words)

@app.route('/bbc/week')
def bbc_week():
    bbc_words = BBC_WEEK
    title = 'BBC - Top words this week'
    return render_template('bbc.html', title=title, bbc_words=bbc_words)

@app.route('/bbc/month')
def bbc_month():
    bbc_words = BBC_MONTH
    title = 'BBC - Top words this month'
    return render_template('bbc.html', title=title, bbc_words=bbc_words)

@app.route('/bbc/ever')
def bbc_ever():
    bbc_words = BBC_EVER
    title = 'BBC - Top words ever'
    return render_template('bbc.html', title=title, bbc_words=bbc_words)


### NYT Pages ###
@app.route('/nyt/today')
def nyt_today():
    nyt_words = NYT_TODAY
    title = 'New York Times - Top words today'
    return render_template('nyt.html', title=title, nyt_words=nyt_words)

@app.route('/nyt/week')
def nyt_week():
    nyt_words = NYT_WEEK
    title = 'New York Times - Top words this week'
    return render_template('nyt.html', title=title, nyt_words=nyt_words)

@app.route('/nyt/month')
def nyt_month():
    nyt_words = NYT_MONTH
    title = 'New York Times - Top words this month'
    return render_template('nyt.html', title=title, nyt_words=nyt_words)

@app.route('/nyt/ever')
def nyt_ever():
    nyt_words = NYT_EVER
    title = 'New York Times - Top words ever'
    return render_template('nyt.html', title=title, nyt_words=nyt_words)
