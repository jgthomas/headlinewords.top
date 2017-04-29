#!/usr/bin/env python


import json

from flask import Flask, render_template

from funcs import load_words
from constants import TODAYS_WORDS, TOP_WORDS


app = Flask(__name__)


WORDS = load_words(TODAYS_WORDS)[:TOP_WORDS]


@app.route('/')
def display_words(words=WORDS):
    return render_template('index.html', words=words)
