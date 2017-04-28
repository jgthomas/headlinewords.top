#!/usr/bin/env python


import json

from flask import Flask, render_template

from bbc_headlines import TODAYS_WORDS, TOP_WORDS


app = Flask(__name__)


def load_words(words):
    with open(words, 'r') as infile:
        todays_words = json.load(infile)
    return todays_words[:TOP_WORDS]


WORDS = load_words(TODAYS_WORDS)


@app.route('/')
def display_words(words=WORDS):
    return render_template('index.html', words=words)
