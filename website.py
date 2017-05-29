#!/usr/bin/env python


from flask import Flask, render_template
from flask_ask import Ask, statement, question

from constants import TOP_N_WORDS, SHORT_N_WORDS

from query_database import (BBC_TODAY, BBC_WEEK, BBC_MONTH, BBC_EVER,
                            NYT_TODAY, NYT_WEEK, NYT_MONTH, NYT_EVER,
                            just_words)

from current_graphs import (HOMEPAGE_BBC_TITLE_1, HOMEPAGE_NYT_TITLE_1,
                            HOMEPAGE_BBC_PLOT_1, HOMEPAGE_NYT_PLOT_1,
                            BBC_TODAY_TITLE_1, BBC_TODAY_PLOT_1,
                            BBC_TODAY_TITLE_2, BBC_TODAY_PLOT_2,
                            BBC_WEEK_TITLE_1, BBC_WEEK_PLOT_1,
                            BBC_WEEK_TITLE_2, BBC_WEEK_PLOT_2,
                            BBC_MONTH_TITLE_1, BBC_MONTH_PLOT_1,
                            BBC_MONTH_TITLE_2, BBC_MONTH_PLOT_2,
                            BBC_EVER_TITLE_1, BBC_EVER_PLOT_1,
                            BBC_EVER_TITLE_2, BBC_EVER_PLOT_2)


app = Flask(__name__)
ask = Ask(app, "/alexa_skill")


### ALEXA ###
@ask.launch
def start_skill():
    welcome_message = "Pick a news source"
    return question(welcome_message)

@ask.intent('BbcIntent')
def read_top_bbc_words():
    words = just_words(BBC_TODAY[:SHORT_N_WORDS])
    words_message = "The top five from the BBC {}".format(words)
    return statement(words_message) \
           .simple_card(title="Top BBC Words", content=' '.join(words))

@ask.intent('NytIntent')
def read_top_nyt_words():
    words = just_words(NYT_TODAY[:SHORT_N_WORDS])
    words_message = "The top five from the New York Times {}".format(words)
    return statement(words_message) \
           .simple_card(title="Top NYT Words", content=' '.join(words))


### HOMEPAGE ###
@app.route('/')
def home():
    title = 'BBC - Top words today'
    bbc_words = BBC_TODAY[:SHORT_N_WORDS]
    nyt_words = NYT_TODAY[:SHORT_N_WORDS]
    main_graph_title = "Highlights"
    subtitle_1 = "BBC"
    title_1 = HOMEPAGE_BBC_TITLE_1
    graph_1 = HOMEPAGE_BBC_PLOT_1
    subtitle_2 = "NYT"
    title_2 = HOMEPAGE_NYT_TITLE_1
    graph_2 = HOMEPAGE_NYT_PLOT_1
    return render_template('index.html',
                           title=title,
                           bbc_words=bbc_words,
                           nyt_words=nyt_words,
                           main_graph_title=main_graph_title,
                           subtitle_1=subtitle_1,
                           title_1=title_1,
                           graph_1=graph_1,
                           subtitle_2=subtitle_2,
                           title_2=title_2,
                           graph_2=graph_2)


### BBC PAGES ###
@app.route('/bbc/today')
def bbc_today():
    title = 'BBC - Top words today'
    bbc_words = BBC_TODAY[:TOP_N_WORDS]
    main_graph_title = "Recent Trends"
    title_1 = BBC_TODAY_TITLE_1
    graph_1 = BBC_TODAY_PLOT_1
    title_2 = BBC_TODAY_TITLE_2
    graph_2 = BBC_TODAY_PLOT_2
    return render_template('bbc.html',
                           title=title,
                           bbc_words=bbc_words,
                           main_graph_title=main_graph_title,
                           title_1=title_1,
                           graph_1=graph_1,
                           title_2=title_2,
                           graph_2=graph_2)

@app.route('/bbc/week')
def bbc_week():
    title = 'BBC - Top words this week'
    bbc_words = BBC_WEEK[:TOP_N_WORDS]
    main_graph_title = "This Week"
    title_1 = BBC_WEEK_TITLE_1
    graph_1 = BBC_WEEK_PLOT_1
    title_2 = BBC_WEEK_TITLE_2
    graph_2 = BBC_WEEK_PLOT_2
    return render_template('bbc.html',
                           title=title,
                           bbc_words=bbc_words,
                           main_graph_title=main_graph_title,
                           title_1=title_1,
                           graph_1=graph_1,
                           title_2=title_2,
                           graph_2=graph_2)

@app.route('/bbc/month')
def bbc_month():
    title = 'BBC - Top words this month'
    bbc_words = BBC_MONTH[:TOP_N_WORDS]
    main_graph_title = "This Month"
    title_1 = BBC_MONTH_TITLE_1
    graph_1 = BBC_MONTH_PLOT_1
    title_2 = BBC_MONTH_TITLE_2
    graph_2 = BBC_MONTH_PLOT_2
    return render_template('bbc.html',
                           title=title,
                           bbc_words=bbc_words,
                           main_graph_title=main_graph_title,
                           title_1=title_1,
                           graph_1=graph_1,
                           title_2=title_2,
                           graph_2=graph_2)

@app.route('/bbc/ever')
def bbc_ever():
    title = 'BBC - Top words ever'
    bbc_words = BBC_EVER[:TOP_N_WORDS]
    main_graph_title = "This Ever"
    title_1 = BBC_EVER_TITLE_1
    graph_1 = BBC_EVER_PLOT_1
    title_2 = BBC_EVER_TITLE_2
    graph_2 = BBC_EVER_PLOT_2
    return render_template('bbc.html',
                           title=title,
                           bbc_words=bbc_words,
                           main_graph_title=main_graph_title,
                           title_1=title_1,
                           graph_1=graph_1,
                           title_2=title_2,
                           graph_2=graph_2)


### NYT PAGES ###
@app.route('/nyt/today')
def nyt_today():
    nyt_words = NYT_TODAY[:TOP_N_WORDS]
    title = 'New York Times - Top words today'
    return render_template('nyt.html', title=title, nyt_words=nyt_words)

@app.route('/nyt/week')
def nyt_week():
    nyt_words = NYT_WEEK[:TOP_N_WORDS]
    title = 'New York Times - Top words this week'
    return render_template('nyt.html', title=title, nyt_words=nyt_words)

@app.route('/nyt/month')
def nyt_month():
    nyt_words = NYT_MONTH[:TOP_N_WORDS]
    title = 'New York Times - Top words this month'
    return render_template('nyt.html', title=title, nyt_words=nyt_words)

@app.route('/nyt/ever')
def nyt_ever():
    nyt_words = NYT_EVER[:TOP_N_WORDS]
    title = 'New York Times - Top words ever'
    return render_template('nyt.html', title=title, nyt_words=nyt_words)
