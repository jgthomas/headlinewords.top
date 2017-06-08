from flask import Blueprint, render_template

from constants import (DML_BASE,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from trending_words import trends
from graph import get_plot


dml = Blueprint("dml", __name__)


@dml.route('/today')
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


@dml.route('/week')
def dml_week():
    title = 'Daily Mail - Top words this week'
    main_data = {**DML_BASE, **{"data": data("dml", "since", "week")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)


@dml.route('/month')
def dml_month():
    title = 'Daily Mail - Top words this month'
    main_data = {**DML_BASE, **{"data": data("dml", "since", "month")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = TOP_N_WORDS)


@dml.route('/ever')
def dml_ever():
    title = 'Daily Mail - Top words ever'
    main_data = {**DML_BASE, **{"data": data("dml", "ever")}}
    return render_template('source.html',
                           title = title,
                           source = main_data,
                           display = DOUBLE_N_WORDS)
