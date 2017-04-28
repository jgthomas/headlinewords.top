#!/usr/bin/env python


from flask import Flask, render_template

app = Flask(__name__)

words = [('cat', 6), ('dog', 3), ('duck', 2)]

@app.route('/')
def display_words(words=words):
    return render_template('index.html', words=words)
