#!/usr/bin/env python


from flask import Flask, render_template
from flask_ask import Ask, statement, question

from constants import (SHORT_N_WORDS, TOP_N_WORDS, DOUBLE_N_WORDS,
                       BBC_BASE, NYT_BASE, DML_BASE, FOX_BASE)

from query_functions import just_words
from query import data
from trending_words import trends
from graph import get_plot


app = Flask(__name__)
ask = Ask(app, "/alexa_skill")


### ALEXA ###
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


### HOMEPAGE ###
@app.route('/')
def home():
    bbc_data = {**BBC_BASE, **{"data": data("bbc", "ondate", "today")}}
    nyt_data = {**NYT_BASE, **{"data": data("nyt", "ondate", "today")}}
    dml_data = {**DML_BASE, **{"data": data("dml", "ondate", "today")}}
    fox_data = {**FOX_BASE, **{"data": data("fox", "ondate", "today")}}
    plot_1 = get_plot(title="Manchester",
                      filename="homepage_bbc_1.png",
                      source="BBC")
    plot_2 = get_plot(title="All Trump, all the time",
                      filename="homepage_nyt_1.png",
                      source="NYT")
    #more = [["Trending", "Words going up and down"],
    #        ["Country", "The USA vs the UK"],
    #        ["Politics", "Left vs right leaning"],
    #        ["By Month", "Each source, each month"]]
    return render_template('index.html',
                           title = 'BBC - Top words today',
                           sources = (bbc_data, nyt_data,
                                      dml_data, fox_data),
                           display = SHORT_N_WORDS,
                           plots = (plot_1, plot_2))
                           #more = more)

### BBC PAGES ###
@app.route('/bbc/today')
def bbc_today():
    title = 'BBC - Top words today'
    main_data = {**BBC_BASE, **{"data": data("bbc", "ondate", "today")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("bbc", "day_on_day")
    plot_1 = get_plot(title="Talking about the parties",
                      filename="bbc_today_1.png")
    plot_2 = get_plot(title="Danger!",
                      filename="bbc_today_2.png")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS,
                           extras = (extra_data_1, extra_data_2),
                           extra_display = SHORT_N_WORDS,
                           plots = (plot_1, plot_2))


@app.route('/bbc/week')
def bbc_week():
    title = 'BBC - Top words today'
    main_data = {**BBC_BASE, **{"data": data("bbc", "since", "week")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("bbc", "week_on_week")
    plot_1 = get_plot(title="Top five progress",
                      filename="bbc_week_1.png")
    plot_2 = get_plot(title="Follow the leader",
                      filename="bbc_week_2.png")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS,
                           extras = (extra_data_1, extra_data_2),
                           extra_display = SHORT_N_WORDS,
                           plots = (plot_1, plot_2))


@app.route('/bbc/month')
def bbc_month():
    title = 'BBC - Top words this month'
    main_data = {**BBC_BASE, **{"data": data("bbc", "since", "month")}}
    plot_1 = get_plot(title="Top five progress",
                      filename="bbc_month_1.png")
    plot_2 = get_plot(title="The grimmest reaper",
                      filename="bbc_month_2.png")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS,
                           plots = (plot_1, plot_2))


@app.route('/bbc/ever')
def bbc_ever():
    title = 'BBC - Top words ever'
    main_data = {**BBC_BASE, **{"data": data("bbc", "ever")}}
    extra_data_1 = {"title": "May",
                    "data": data("bbc", "between", "may_start", "jun_start")}
    extra_data_2 = {"title": "June",
                    "data": data("bbc", "between", "jun_start", "jul_start")}
    plot_1 = get_plot(title="Top five progress",
                      filename="bbc_ever_1.png")
    plot_2 = get_plot(title="City limits",
                      filename="bbc_ever_2.png")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = DOUBLE_N_WORDS,
                           extras = (extra_data_1, extra_data_2),
                           extra_display = TOP_N_WORDS,
                           plots = (plot_1, plot_2))


### NYT PAGES ###
@app.route('/nyt/today')
def nyt_today():
    title = 'New York Times - Top words today'
    main_data = {**NYT_BASE, **{"data": data("nyt", "ondate", "today")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("nyt", "day_on_day")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS,
                           extras = (extra_data_1, extra_data_2),
                           extra_display = SHORT_N_WORDS)


@app.route('/nyt/week')
def nyt_week():
    title = 'New York Times - Top words this week'
    main_data = {**NYT_BASE, **{"data": data("nyt", "since", "week")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("nyt", "week_on_week")
    plot_1 = get_plot(title="Top five progress",
                      filename="nyt_week_1.png")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS,
                           extras = (extra_data_1, extra_data_2),
                           extra_display = SHORT_N_WORDS,
                           plots = (plot_1,))


@app.route('/nyt/month')
def nyt_month():
    title = 'New York Times - Top words this month'
    main_data = {**NYT_BASE, **{"data": data("nyt", "since", "month")}}
    plot_1 = get_plot(title="The Trumps",
                      filename="nyt_month_1.png")
    plot_2 = get_plot(title="The investigation",
                      filename="nyt_month_2.png")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS,
                           plots = (plot_1, plot_2))


@app.route('/nyt/ever')
def nyt_ever():
    title = 'New York Times - Top words ever'
    main_data = {**NYT_BASE, **{"data": data("nyt", "ever")}}
    extra_data_1 = {"title": "May",
                    "data": data("nyt", "between", "may_start", "jun_start")}
    extra_data_2 = {"title": "June",
                    "data": data("nyt", "between", "jun_start", "jul_start")}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = DOUBLE_N_WORDS,
                           extras = (extra_data_1, extra_data_2),
                           extra_display = TOP_N_WORDS)



#### DAILY MAIL ###
@app.route('/dml/today')
def dml_today():
    title = 'Daily Mail - Top words today'
    main_data = {**DML_BASE, **{"data": data("dml", "ondate", "today")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("dml", "day_on_day")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS,
                           extras = (extra_data_1, extra_data_2),
                           extra_display = SHORT_N_WORDS)


@app.route('/dml/week')
def dml_week():
    title = 'Daily Mail - Top words this week'
    main_data = {**DML_BASE, **{"data": data("dml", "since", "week")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)


@app.route('/dml/month')
def dml_month():
    title = 'Daily Mail - Top words this month'
    main_data = {**DML_BASE, **{"data": data("dml", "since", "month")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)


@app.route('/dml/ever')
def dml_ever():
    title = 'Daily Mail - Top words ever'
    main_data = {**DML_BASE, **{"data": data("dml", "ever")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = DOUBLE_N_WORDS)



### FOX NEWS ###
@app.route('/fox/today')
def fox_today():
    title = 'Fox News - Top words today'
    main_data = {**FOX_BASE, **{"data": data("fox", "ondate", "today")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("fox", "day_on_day")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS,
                           extras = (extra_data_1, extra_data_2),
                           extra_display = SHORT_N_WORDS)


@app.route('/fox/week')
def fox_week():
    title = 'Fox News - Top words this week',
    main_data = {**FOX_BASE, **{"data": data("fox", "since", "week")}}
    return render_template('source.html',
                           title = 'Fox News - Top words this week',
                           source = main_data,
                           display = TOP_N_WORDS)


@app.route('/fox/month')
def fox_month():
    title = 'Fox News - Top words this month'
    main_data = {**FOX_BASE, **{"data": data("fox", "since", "month")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)


@app.route('/fox/ever')
def fox_ever():
    title = 'Fox News - Top words ever'
    main_data = {**FOX_BASE, **{"data": data("fox", "ever")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = DOUBLE_N_WORDS)
