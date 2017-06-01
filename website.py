#!/usr/bin/env python


from flask import Flask, render_template
from flask_ask import Ask, statement, question

from constants import TOP_N_WORDS, SHORT_N_WORDS, MAX_N_WORDS, HIGH_N_WORDS, DOUBLE_N_WORDS

from query_functions import just_words

from query import data

from standing_queries import (BBC_TODAY, BBC_WEEK, BBC_MONTH, BBC_EVER,
                              NYT_TODAY, NYT_WEEK, NYT_MONTH, NYT_EVER,
                              BBC_TODAY_RISING, BBC_TODAY_FALLING,
                              BBC_WEEK_RISING, BBC_WEEK_FALLING,
                              NYT_TODAY_RISING, NYT_TODAY_FALLING,
                              NYT_WEEK_RISING, NYT_WEEK_FALLING)

from graph_configs import (HOMEPAGE_BBC_1, HOMEPAGE_NYT_1,
                           BBC_TODAY_1, BBC_TODAY_2,
                           BBC_WEEK_1, BBC_WEEK_2,
                           BBC_MONTH_1, BBC_MONTH_2,
                           BBC_EVER_1, BBC_EVER_2,
                           NYT_WEEK_1,
                           NYT_MONTH_1, NYT_MONTH_2)


app = Flask(__name__)
ask = Ask(app, "/alexa_skill")


### ALEXA ###
@ask.launch
def start_skill():
    welcome_message = "Pick a news source"
    return question(welcome_message)

@ask.intent('BbcIntent')
def read_top_bbc_words():
    words = just_words(BBC_TODAY["data"][:SHORT_N_WORDS])
    words_message = "The top five from the BBC {}".format(words)
    return statement(words_message) \
           .simple_card(title="Top BBC Words", content=' '.join(words))

@ask.intent('NytIntent')
def read_top_nyt_words():
    words = just_words(NYT_TODAY["data"][:SHORT_N_WORDS])
    words_message = "The top five from the New York Times {}".format(words)
    return statement(words_message) \
           .simple_card(title="Top NYT Words", content=' '.join(words))


### HOMEPAGE ###
@app.route('/')
def home():
    NEW_SOURCE_1 = {"title": "Daily Mail",
                    "data": data('dml', 'ondate', 'today')}
    NEW_SOURCE_2 = {"title": "Fox News",
                    "data": data('fox', 'ondate', 'today')}
    return render_template('index.html',
                           title = 'BBC - Top words today',
                           sources = (BBC_TODAY, NYT_TODAY,
                                      NEW_SOURCE_1, NEW_SOURCE_2),
                           display = SHORT_N_WORDS,
                           plots = (HOMEPAGE_BBC_1, HOMEPAGE_NYT_1))

### BBC PAGES ###
@app.route('/bbc/today')
def bbc_today():
    return render_template('bbc.html',
                           title = 'BBC - Top words today',
                           source = BBC_TODAY,
                           display = TOP_N_WORDS,
                           extras = (BBC_TODAY_RISING, BBC_TODAY_FALLING),
                           extra_display = SHORT_N_WORDS,
                           plots = (BBC_TODAY_1, BBC_TODAY_2))

@app.route('/bbc/week')
def bbc_week():
    return render_template('bbc.html',
                           title = 'BBC - Top words this week',
                           source = BBC_WEEK,
                           display = TOP_N_WORDS,
                           extras = (BBC_WEEK_RISING, BBC_WEEK_FALLING),
                           extra_display = SHORT_N_WORDS,
                           plots = (BBC_WEEK_1, BBC_WEEK_2))

@app.route('/bbc/month')
def bbc_month():
    return render_template('bbc.html',
                           title = 'BBC - Top words this month',
                           source = BBC_MONTH,
                           display = TOP_N_WORDS,
                           plots = (BBC_MONTH_1, BBC_MONTH_2))

@app.route('/bbc/ever')
def bbc_ever():
    MAY = {"title": "May",
           "data": data("bbc", "between", "may_start", "jun_start")}
    JUNE = {"title": "June",
            "data": data("bbc", "between", "jun_start", "jul_start")}
    return render_template('bbc.html',
                           title = 'BBC - Top words ever',
                           source = BBC_EVER,
                           display = DOUBLE_N_WORDS,
                           extras = (MAY, JUNE),
                           extra_display = TOP_N_WORDS,
                           plots = (BBC_EVER_1, BBC_EVER_2))


### NYT PAGES ###
@app.route('/nyt/today')
def nyt_today():
    return render_template('nyt.html',
                           title = 'New York Times - Top words today',
                           source = NYT_TODAY,
                           display = TOP_N_WORDS,
                           extras = (NYT_TODAY_RISING, NYT_TODAY_FALLING),
                           extra_display = SHORT_N_WORDS)

@app.route('/nyt/week')
def nyt_week():
    return render_template('nyt.html',
                           title = 'New York Times - Top words this week',
                           source = NYT_WEEK,
                           display = TOP_N_WORDS,
                           extras = (NYT_WEEK_RISING, NYT_WEEK_FALLING),
                           extra_display = SHORT_N_WORDS,
                           plots = (NYT_WEEK_1,))

@app.route('/nyt/month')
def nyt_month():
    return render_template('nyt.html',
                           title = 'New York Times - Top words this month',
                           source = NYT_MONTH,
                           display = TOP_N_WORDS,
                           plots = (NYT_MONTH_1, NYT_MONTH_2))

@app.route('/nyt/ever')
def nyt_ever():
    MAY = {"title": "May",
           "data": data("nyt", "between", "may_start", "jun_start")}
    JUNE = {"title": "June",
            "data": data("nyt", "between", "jun_start", "jul_start")}
    return render_template('nyt.html',
                           title = 'New York Times - Top words ever',
                           source = NYT_EVER,
                           display = DOUBLE_N_WORDS,
                           extras = (MAY, JUNE),
                           extra_display = TOP_N_WORDS)


### COMBINED PAGES ###
@app.route('/top200')
def top_200():
    return render_template('top_many.html',
            title = 'Comparative top 200 words',
            how_many = 'Top 200',
            sources = (BBC_EVER, NYT_EVER),
            display = HIGH_N_WORDS)
