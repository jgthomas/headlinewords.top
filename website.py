#!/usr/bin/env python


import json

from flask import Flask, render_template

from funcs import load_words
from constants import (TODAYS_WORDS, 
                       TOP_WORDS,
                       WEEK,
                       MONTH)

from query_database import (query, 
                            overall_total,
                            since_date)

app = Flask(__name__)


WORDS = load_words(TODAYS_WORDS)[:TOP_WORDS]
WEEK_WORDS = query(since_date, (WEEK,))[:TOP_WORDS]
MONTH_WORDS = query(since_date, (MONTH,))[:TOP_WORDS]
EVER_WORDS = query(overall_total)[:TOP_WORDS]
ALL_WORDS = query(overall_total)


@app.route('/')
def now(words=WORDS):
    return render_template('now.html', words=words)


@app.route('/week')
def week(words=WEEK_WORDS):
    return render_template('week.html', words=WEEK_WORDS)


@app.route('/month')
def month(words=MONTH_WORDS):
    return render_template('month.html', words=MONTH_WORDS)


@app.route('/ever')
def ever(words=EVER_WORDS):
    return render_template('ever.html', words=EVER_WORDS)


@app.route('/all')
def all(words=ALL_WORDS):
    return render_template('all.html', words=ALL_WORDS)
