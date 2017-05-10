#!/usr/bin/env python


import json

from flask import Flask, render_template

from funcs import load_words

from constants import (TODAYS_WORDS, 
                       TOP_WORDS,
                       TODAY,
                       WEEK,
                       MONTH,
                       DATABASE,
                       BBC_DATABASE)

from query_database import (query, 
                            query_database,
                            specific_date,
                            overall_total,
                            since_date)

app = Flask(__name__)


#WORDS = load_words(TODAYS_WORDS)[:TOP_WORDS]
#WEEK_WORDS = query(since_date, (WEEK,))[:TOP_WORDS]
#MONTH_WORDS = query(since_date, (MONTH,))[:TOP_WORDS]
#EVER_WORDS = query(overall_total)[:TOP_WORDS]
#ALL_WORDS = query(overall_total)

# BBC
WORDS = query_database(BBC_DATABASE, specific_date, (TODAY,))[:TOP_WORDS]
WEEK_WORDS = query_database(BBC_DATABASE, since_date, (WEEK,))[:TOP_WORDS]
MONTH_WORDS = query_database(BBC_DATABASE, since_date, (MONTH,))[:TOP_WORDS]
EVER_WORDS = query_database(BBC_DATABASE, overall_total)[:TOP_WORDS]
ALL_WORDS = query_database(BBC_DATABASE, overall_total)


@app.route('/')
def now():
    words = WORDS
    title = 'Top words today'
    return render_template('query_output.html', title=title, words=words)


#@app.route('/')
#def now():
#    words = WORDS
#    title = 'Top words right now'
#    return render_template('now.html', title=title, words=words)


@app.route('/week')
def week():
    words = WEEK_WORDS
    title = 'Top words this week'
    return render_template('query_output.html', title=title, words=words)


@app.route('/month')
def month():
    words = MONTH_WORDS
    title = 'Top words this month'
    return render_template('query_output.html', title=title, words=words)


@app.route('/ever')
def ever():
    words = EVER_WORDS
    title = 'Top words ever'
    return render_template('query_output.html', title=title, words=words)


@app.route('/all')
def all():
    words = ALL_WORDS
    title = 'Complete list'
    return render_template('query_output.html', title=title, words=words)
