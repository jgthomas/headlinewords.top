#!/usr/bin/env python


from flask import Flask, render_template
from flask_ask import Ask, statement, question

from constants import (TOP_N_WORDS,
                       TODAY,
                       WEEK,
                       MONTH,
                       BBC_DATABASE,
                       NYT_DATABASE)

from query_database import (query,
                            specific_date,
                            overall_total,
                            since_date)

app = Flask(__name__)
ask = Ask(app, "/alexa_skill")


### Queries ###
BBC_TOP = query(BBC_DATABASE, specific_date, (TODAY,))[:5]
NYT_TOP = query(NYT_DATABASE, specific_date, (TODAY,))[:5]

BBC_TODAY = query(BBC_DATABASE, specific_date, (TODAY,))[:TOP_N_WORDS]
BBC_WEEK = query(BBC_DATABASE, since_date, (WEEK,))[:TOP_N_WORDS]
BBC_MONTH = query(BBC_DATABASE, since_date, (MONTH,))[:TOP_N_WORDS]
BBC_EVER = query(BBC_DATABASE, overall_total)[:TOP_N_WORDS]

NYT_TODAY = query(NYT_DATABASE, specific_date, (TODAY,))[:TOP_N_WORDS]
NYT_WEEK = query(NYT_DATABASE, since_date, (WEEK,))[:TOP_N_WORDS]
NYT_MONTH = query(NYT_DATABASE, since_date, (MONTH,))[:TOP_N_WORDS]
NYT_EVER = query(NYT_DATABASE, overall_total)[:TOP_N_WORDS]


def just_words(data):
    words = []
    for word, *rest in data:
        words.append(word)
    return words


### Alexa ###
@ask.launch
def start_skill():
    welcome_message = "Pick a news source"
    return question(welcome_message)


@ask.intent('BbcIntent')
def read_top_bbc_words():
    words = just_words(BBC_TOP)
    words_message = "The top five words today are {}".format(words)
    return statement(words_message)


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
