#!/usr/bin/env python

from flask import Flask, render_template
from flask_ask import Ask, statement, question

from constants import (SHORT_N_WORDS,
                       BBC_BASE, NYT_BASE,
                       DML_BASE, FOX_BASE,
                       SMH_BASE, ABC_BASE)

from query_functions import just_words
from query import data
from graph import get_plot

from publications.bbc_pages import bbc
from publications.nyt_pages import nyt
from publications.dml_pages import dml
from publications.fox_pages import fox
from publications.smh_pages import smh
from publications.abc_pages import abc

from overviews.by_country import by_country


app = Flask(__name__)

app.register_blueprint(bbc, url_prefix='/bbc')
app.register_blueprint(nyt, url_prefix='/nyt')
app.register_blueprint(dml, url_prefix='/dml')
app.register_blueprint(fox, url_prefix='/fox')
app.register_blueprint(smh, url_prefix='/smh')
app.register_blueprint(abc, url_prefix='/abc')
app.register_blueprint(by_country, url_prefix='/country')

ask = Ask(app, "/alexa_skill")


@app.route('/')
def home():
    bbc_data = {**BBC_BASE, **{"data": data("bbc", "ondate", "today")}}
    nyt_data = {**NYT_BASE, **{"data": data("nyt", "ondate", "today")}}
    dml_data = {**DML_BASE, **{"data": data("dml", "ondate", "today")}}
    fox_data = {**FOX_BASE, **{"data": data("fox", "ondate", "today")}}
    smh_data = {**SMH_BASE, **{"data": data("smh", "ondate", "today")}}
    abc_data = {**ABC_BASE, **{"data": data("abc", "ondate", "today")}}
    plot_1 = get_plot(title="Manchester, then London",
                      filename="homepage_bbc_1.png",
                      source="BBC")
    plot_2 = get_plot(title="All Trump, all the time",
                      filename="homepage_nyt_1.png",
                      source="NYT")
    return render_template('index.html',
                           title='All top words today',
                           sources=(bbc_data, nyt_data,
                                    dml_data, fox_data,
                                    smh_data, abc_data),
                           display=SHORT_N_WORDS,
                           plots=(plot_1, plot_2))


@ask.launch
def start_skill():
    welcome_message = "Pick a news source"
    return question(welcome_message)

@ask.intent('BbcIntent')
def read_top_bbc_words():
    words = just_words(data("bbc", "ondate", "today"))[:SHORT_N_WORDS]
    words_message = "The top five from the BBC {}".format(words)
    return statement(words_message) \
           .simple_card(title="Top BBC Words", content=' '.join(words))

@ask.intent('NytIntent')
def read_top_nyt_words():
    words = just_words(data("nyt", "ondate", "today"))[:SHORT_N_WORDS]
    words_message = "The top five from the New York Times {}".format(words)
    return statement(words_message) \
           .simple_card(title="Top NYT Words", content=' '.join(words))
