#!/usr/bin/env python


from flask import Flask, render_template
from flask_ask import Ask, statement, question

from constants import TOP_N_WORDS, SHORT_N_WORDS, MAX_N_WORDS, HIGH_N_WORDS, DOUBLE_N_WORDS

from query_functions import just_words

from query import data

from standing_queries import *

from graph_configs import *


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
    return render_template('index.html',
                           title = 'BBC - Top words today',
                           sources = (BBC_TODAY, NYT_TODAY,
                                      DML_TODAY, FOX_TODAY),
                           display = SHORT_N_WORDS,
                           plots = (HOMEPAGE_BBC_1, HOMEPAGE_NYT_1))

### BBC PAGES ###
@app.route('/bbc/today')
def bbc_today():
    return render_template('source.html',
                           title = 'BBC - Top words today',
                           source = BBC_TODAY,
                           display = TOP_N_WORDS,
                           extras = (BBC_TODAY_RISING, BBC_TODAY_FALLING),
                           extra_display = SHORT_N_WORDS,
                           plots = (BBC_TODAY_1, BBC_TODAY_2))

@app.route('/bbc/week')
def bbc_week():
    return render_template('source.html',
                           title = 'BBC - Top words this week',
                           source = BBC_WEEK,
                           display = TOP_N_WORDS,
                           extras = (BBC_WEEK_RISING, BBC_WEEK_FALLING),
                           extra_display = SHORT_N_WORDS,
                           plots = (BBC_WEEK_1, BBC_WEEK_2))

@app.route('/bbc/month')
def bbc_month():
    return render_template('source.html',
                           title = 'BBC - Top words this month',
                           source = BBC_MONTH,
                           display = TOP_N_WORDS,
                           plots = (BBC_MONTH_1, BBC_MONTH_2))

@app.route('/bbc/ever')
def bbc_ever():
    return render_template('source.html',
                           title = 'BBC - Top words ever',
                           source = BBC_EVER,
                           display = DOUBLE_N_WORDS,
                           extras = (BBC_MAY, BBC_JUN),
                           extra_display = TOP_N_WORDS,
                           plots = (BBC_EVER_1, BBC_EVER_2))


### NYT PAGES ###
@app.route('/nyt/today')
def nyt_today():
    return render_template('source.html',
                           title = 'New York Times - Top words today',
                           source = NYT_TODAY,
                           display = TOP_N_WORDS,
                           extras = (NYT_TODAY_RISING, NYT_TODAY_FALLING),
                           extra_display = SHORT_N_WORDS)

@app.route('/nyt/week')
def nyt_week():
    return render_template('source.html',
                           title = 'New York Times - Top words this week',
                           source = NYT_WEEK,
                           display = TOP_N_WORDS,
                           extras = (NYT_WEEK_RISING, NYT_WEEK_FALLING),
                           extra_display = SHORT_N_WORDS,
                           plots = (NYT_WEEK_1,))

@app.route('/nyt/month')
def nyt_month():
    return render_template('source.html',
                           title = 'New York Times - Top words this month',
                           source = NYT_MONTH,
                           display = TOP_N_WORDS,
                           plots = (NYT_MONTH_1, NYT_MONTH_2))

@app.route('/nyt/ever')
def nyt_ever():
    return render_template('source.html',
                           title = 'New York Times - Top words ever',
                           source = NYT_EVER,
                           display = DOUBLE_N_WORDS,
                           extras = (NYT_MAY, NYT_JUN),
                           extra_display = TOP_N_WORDS)

### DAILY MAIL ###
@app.route('/dml/today')
def dml_today():
    return render_template('source.html',
                           title = 'Daily Mail - Top words today',
                           source = DML_TODAY,
                           display = TOP_N_WORDS,
                           extras = (DML_TODAY_RISING, DML_TODAY_FALLING),
                           extra_display = SHORT_N_WORDS)
@app.route('/dml/week')
def dml_week():
    return render_template('source.html',
                           title = 'Daily Mail - Top words this week',
                           source = DML_WEEK,
                           display = TOP_N_WORDS)
@app.route('/dml/month')
def dml_month():
    return render_template('source.html',
                           title = 'Daily Mail - Top words this month',
                           source = DML_MONTH,
                           display = TOP_N_WORDS)
@app.route('/dml/ever')
def dml_ever():
    return render_template('source.html',
                           title = 'Daily Mail - Top words ever',
                           source = DML_EVER,
                           display = DOUBLE_N_WORDS)


### FOX NEWS ###
@app.route('/fox/today')
def fox_today():
    return render_template('source.html',
                           title = 'Fox News - Top words today',
                           source = FOX_TODAY,
                           display = TOP_N_WORDS,
                           extras = (FOX_TODAY_RISING, FOX_TODAY_FALLING),
                           extra_display = SHORT_N_WORDS)
@app.route('/fox/week')
def fox_week():
    return render_template('source.html',
                           title = 'Fox News - Top words this week',
                           source = FOX_WEEK,
                           display = TOP_N_WORDS)
@app.route('/fox/month')
def fox_month():
    return render_template('source.html',
                           title = 'Fox News - Top words this month',
                           source = FOX_MONTH,
                           display = TOP_N_WORDS)
@app.route('/fox/ever')
def fox_ever():
    return render_template('source.html',
                           title = 'Fox News - Top words ever',
                           source = FOX_EVER,
                           display = DOUBLE_N_WORDS)


### COMBINED PAGES ###
@app.route('/top200')
def top_200():
    return render_template('top_many.html',
            title = 'Comparative top 200 words',
            how_many = 'Top 200',
            sources = (BBC_EVER, NYT_EVER),
            display = HIGH_N_WORDS)
