#!/usr/bin/env python


import json

from flask import Flask, render_template

from funcs import load_words
from constants import TODAYS_WORDS, TOP_WORDS

from query_database import query, overall_total


app = Flask(__name__)


WORDS = load_words(TODAYS_WORDS)[:TOP_WORDS]
ALL_TIME_WORDS = query(overall_total)[:TOP_WORDS]
ALL_WORDS = query(overall_total)


@app.route('/')
def display_words(words=WORDS):
    return render_template('words_now.html', words=words)


@app.route('/alltime')
def show_all_time_words(words=ALL_TIME_WORDS):
    return render_template('words_alltime.html', words=ALL_TIME_WORDS)


@app.route('/all')
def show_all_words(words=ALL_WORDS):
    return render_template('words_all.html', words=ALL_WORDS)
