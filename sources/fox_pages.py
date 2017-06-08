from flask import Blueprint, render_template

from constants import (FOX_BASE,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from trending_words import trends


fox = Blueprint("fox", __name__)


@fox.route('/today')
def fox_today():
    title = 'Fox News - Top words today'
    main_data = {**FOX_BASE, **{"data": data("fox", "ondate", "today")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("fox", "day_on_day")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@fox.route('/week')
def fox_week():
    title = 'Fox News - Top words this week',
    main_data = {**FOX_BASE, **{"data": data("fox", "since", "week")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS)


@fox.route('/month')
def fox_month():
    title = 'Fox News - Top words this month'
    main_data = {**FOX_BASE, **{"data": data("fox", "since", "month")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS)


@fox.route('/ever')
def fox_ever():
    title = 'Fox News - Top words ever'
    main_data = {**FOX_BASE, **{"data": data("fox", "ever")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=DOUBLE_N_WORDS)
