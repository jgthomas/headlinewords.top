#!/usr/bin/env python


from flask import Flask, render_template

from constants import (TOP_N_WORDS,
                       TODAY,
                       WEEK,
                       MONTH,
                       BBC_DATABASE)

from query_database import (query,
                            specific_date,
                            overall_total,
                            since_date)

app = Flask(__name__)

BBC_TODAY = query(BBC_DATABASE, specific_date, (TODAY,))[:TOP_N_WORDS]
BBC_WEEK = query(BBC_DATABASE, since_date, (WEEK,))[:TOP_N_WORDS]
BBC_MONTH = query(BBC_DATABASE, since_date, (MONTH,))[:TOP_N_WORDS]
BBC_EVER = query(BBC_DATABASE, overall_total)[:TOP_N_WORDS]
BBC_ALL = query(BBC_DATABASE, overall_total)

@app.route('/')
def today():
    words = BBC_TODAY
    title = 'Top words today'
    return render_template('query_output.html', title=title, words=words)

@app.route('/week')
def week():
    words = BBC_WEEK
    title = 'Top words this week'
    return render_template('query_output.html', title=title, words=words)

@app.route('/month')
def month():
    words = BBC_MONTH
    title = 'Top words this month'
    return render_template('query_output.html', title=title, words=words)

@app.route('/ever')
def ever():
    words = BBC_EVER
    title = 'Top words ever'
    return render_template('query_output.html', title=title, words=words)

@app.route('/all')
def all():
    words = BBC_ALL
    title = 'Complete list'
    return render_template('query_output.html', title=title, words=words)
