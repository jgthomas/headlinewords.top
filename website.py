#!/usr/bin/env python


from flask import Flask, render_template

from constants import (TOP_WORDS,
                       TODAY,
                       WEEK,
                       MONTH,
                       BBC_DATABASE)

from query_database import (query_database,
                            specific_date,
                            overall_total,
                            since_date)

app = Flask(__name__)

BBC_WORDS = query_database(BBC_DATABASE, specific_date, (TODAY,))[:TOP_WORDS]
BBC_WEEK_WORDS = query_database(BBC_DATABASE, since_date, (WEEK,))[:TOP_WORDS]
BBC_MONTH_WORDS = query_database(BBC_DATABASE, since_date, (MONTH,))[:TOP_WORDS]
BBC_EVER_WORDS = query_database(BBC_DATABASE, overall_total)[:TOP_WORDS]
BBC_ALL_WORDS = query_database(BBC_DATABASE, overall_total)

@app.route('/')
def today():
    words = BBC_WORDS
    title = 'Top words today'
    return render_template('query_output.html', title=title, words=words)

@app.route('/week')
def week():
    words = BBC_WEEK_WORDS
    title = 'Top words this week'
    return render_template('query_output.html', title=title, words=words)

@app.route('/month')
def month():
    words = BBC_MONTH_WORDS
    title = 'Top words this month'
    return render_template('query_output.html', title=title, words=words)

@app.route('/ever')
def ever():
    words = BBC_EVER_WORDS
    title = 'Top words ever'
    return render_template('query_output.html', title=title, words=words)

@app.route('/all')
def all():
    words = BBC_ALL_WORDS
    title = 'Complete list'
    return render_template('query_output.html', title=title, words=words)
