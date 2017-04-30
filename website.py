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
ALL_TIME_WORDS = query(overall_total)[:TOP_WORDS]
ALL_WORDS = query(overall_total)


@app.route('/')
def display_words(words=WORDS):
    return render_template('words_now.html', words=words)


@app.route('/week')
def show_week_words(words=WEEK_WORDS):
    return render_template('words_week.html', words=WEEK_WORDS)


@app.route('/month')
def show_month_words(words=MONTH_WORDS):
    return render_template('words_month.html', words=MONTH_WORDS)


@app.route('/alltime')
def show_all_time_words(words=ALL_TIME_WORDS):
    return render_template('words_alltime.html', words=ALL_TIME_WORDS)


@app.route('/all')
def show_all_words(words=ALL_WORDS):
    return render_template('words_all.html', words=ALL_WORDS)
