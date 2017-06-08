#!/usr/bin/env python


from flask import Flask, render_template
from flask_ask import Ask, statement, question

from constants import (SHORT_N_WORDS, TOP_N_WORDS, DOUBLE_N_WORDS,
                       BBC_BASE, NYT_BASE, DML_BASE, FOX_BASE,
                       SMH_BASE, ABC_BASE,
                       UK_BASE, US_BASE, AU_BASE)

from query_functions import just_words
from query import data
from trending_words import trends
from graph import get_plot
from composite_counts import composite_ranks


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
    smh_data = {**SMH_BASE, **{"data": data("smh", "ondate", "today")}}
    abc_data = {**ABC_BASE, **{"data": data("abc", "ondate", "today")}}
    plot_1 = get_plot(title="Manchester, then London",
                      filename="homepage_bbc_1.png",
                      source="BBC")
    plot_2 = get_plot(title="All Trump, all the time",
                      filename="homepage_nyt_1.png",
                      source="NYT")
    return render_template('index.html',
                           title = 'All top words today',
                           sources = (bbc_data, nyt_data,
                                      dml_data, fox_data,
                                      smh_data, abc_data),
                           display = SHORT_N_WORDS,
                           plots = (plot_1, plot_2))

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
    plot_1 = get_plot(title="The Trumps",
                      filename="nyt_today_1.png")
    plot_2 = get_plot(title="The investigation",
                      filename="nyt_today_2.png")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS,
                           extras = (extra_data_1, extra_data_2),
                           extra_display = SHORT_N_WORDS,
                           plots = (plot_1, plot_2))


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
    plot_1 = get_plot(title="Top five progress",
                      filename="nyt_month_1.png")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS,
                           plots = (plot_1,))


@app.route('/nyt/ever')
def nyt_ever():
    title = 'New York Times - Top words ever'
    main_data = {**NYT_BASE, **{"data": data("nyt", "ever")}}
    extra_data_1 = {"title": "May",
                    "data": data("nyt", "between", "may_start", "jun_start")}
    extra_data_2 = {"title": "June",
                    "data": data("nyt", "between", "jun_start", "jul_start")}
    plot_1 = get_plot(title="Top five progress",
                      filename="nyt_ever_1.png")
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = DOUBLE_N_WORDS,
                           extras = (extra_data_1, extra_data_2),
                           extra_display = TOP_N_WORDS,
                           plots = (plot_1,))



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


### SYDNEY MORNING HERALD
@app.route('/smh/today')
def smh_today():
    title = 'Sydney Morning Herald - Top words today'
    main_data = {**SMH_BASE, **{"data": data("smh", "ondate", "today")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)

@app.route('/smh/week')
def smh_week():
    title = 'Sydney Morning Herald - Top words this week'
    main_data = {**SMH_BASE, **{"data": data("smh", "since", "week")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)

@app.route('/smh/month')
def smh_month():
    title = 'Sydney Morning Herald - Top words this month'
    main_data = {**SMH_BASE, **{"data": data("smh", "since", "month")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)

@app.route('/smh/ever')
def smh_ever():
    title = 'Sydney Morning Herald - Top words ever'
    main_data = {**SMH_BASE, **{"data": data("smh", "ever")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = DOUBLE_N_WORDS)


### ABC AUSTRALIA
@app.route('/abc/today')
def abc_today():
    title = 'ABC Australia - Top words today'
    main_data = {**ABC_BASE, **{"data": data("abc", "ondate", "today")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)

@app.route('/abc/week')
def abc_week():
    title = 'ABC Australia - Top words this week'
    main_data = {**ABC_BASE, **{"data": data("abc", "since", "week")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)

@app.route('/abc/month')
def abc_month():
    title = 'ABC Australia - Top words this month'
    main_data = {**ABC_BASE, **{"data": data("abc", "since", "month")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)

@app.route('/abc/ever')
def abc_ever():
    title = 'ABC Australia - Top words ever'
    main_data = {**ABC_BASE, **{"data": data("abc", "ever")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = DOUBLE_N_WORDS)





### COMBINED ###
@app.route('/country')
def country_day():
    title = 'By Country - Today'
    page_title = "Country Comparison"
    uk_sources = [data('bbc', 'ondate', 'today'),
                  data('dml', 'ondate', 'today')]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_sources = [data('nyt', 'ondate', 'today'),
                  data('fox', 'ondate', 'today')]
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    au_sources = [data('smh', 'ondate', 'today'),
                  data('abc', 'ondate', 'today')]
    au_combined = {**AU_BASE, **{"data": composite_ranks(au_sources)}}
    return render_template('combined.html',
                           page_title = page_title,
                           title = title,
                           sources = (uk_combined,
                                      us_combined,
                                      au_combined),
                           display = DOUBLE_N_WORDS)

@app.route('/country/week')
def country_week():
    title = 'By Country - This Week'
    page_title = "Country Comparison"
    uk_sources = [data('bbc', 'since', 'week'),
                  data('dml', 'since', 'week')]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_sources = [data('nyt', 'since', 'week'),
                  data('fox', 'since', 'week')]
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    return render_template('combined.html',
                           page_title = page_title,
                           title = title,
                           sources = (uk_combined, us_combined),
                           display = DOUBLE_N_WORDS)

@app.route('/country/month')
def country_month():
    title = 'By Country - This Month'
    page_title = "Country Comparison"
    uk_sources = [data('bbc', 'since', 'month'),
                  data('dml', 'since', 'month')]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_sources = [data('nyt', 'since', 'month'),
                  data('fox', 'since', 'month')]
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    return render_template('combined.html',
                           page_title = page_title,
                           title = title,
                           sources = (uk_combined, us_combined),
                           display = DOUBLE_N_WORDS)

@app.route('/country/ever')
def country_ever():
    title = 'By Country - Ever'
    page_title = "Country Comparison"
    uk_sources = [data('bbc', 'ever'),
                  data('dml', 'ever')]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_sources = [data('nyt', 'ever'),
                  data('fox', 'ever')]
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    return render_template('combined.html',
                           page_title = page_title,
                           title = title,
                           sources = (uk_combined, us_combined),
                           display = DOUBLE_N_WORDS)
