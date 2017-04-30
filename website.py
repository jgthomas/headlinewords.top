#!/usr/bin/env python


import json

from flask import Flask, render_template

from funcs import load_words
from constants import TODAYS_WORDS, TOP_WORDS

from query_database import query, overall_total


app = Flask(__name__)


WORDS = load_words(TODAYS_WORDS)[:TOP_WORDS]

#ALL_TIME_WORDS = query(overall_total)[:TOP_WORDS]


@app.route('/')
def display_words(words=WORDS):
    return render_template('index.html', words=words)


#@app.route('/alltime')
#def show_all_time_words(words=ALL_TIME_WORDS):
#    return render_template('index.html', words=ALL_TIME_WORDS)
