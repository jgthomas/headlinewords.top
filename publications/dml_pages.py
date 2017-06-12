from flask import Blueprint, render_template

from constants import (DML_BASE,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from query_functions import MONTHS, THIS, LAST, NEXT
from trending_words import trends


dml = Blueprint("dml", __name__)


@dml.route('/today')
def dml_today():
    title = 'Daily Mail - Top words today'
    main_data = {**DML_BASE, **{"data": data("dml", "ondate", "today")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("dml", "day_on_day")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@dml.route('/week')
def dml_week():
    title = 'Daily Mail - Top words this week'
    main_data = {**DML_BASE, **{"data": data("dml", "since", "week")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("dml", "week_on_week")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@dml.route('/month')
def dml_month():
    title = 'Daily Mail - Top words this month'
    main_data = {**DML_BASE, **{"data": data("dml", "since", "month")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("dml", "month_on_month")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@dml.route('/ever')
def dml_ever():
    title = 'Daily Mail - Top words ever'
    main_data = {**DML_BASE, **{"data": data("dml", "ever")}}
    extra_data_1 = {"title": MONTHS[LAST]["name"],
                    "data": data("dml", "between", MONTHS[LAST]["start"],
                                                   MONTHS[THIS]["start"])}
    extra_data_2 = {"title": MONTHS[THIS]["name"],
                    "data": data("dml", "between", MONTHS[THIS]["start"],
                                                   MONTHS[NEXT]["start"])}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=DOUBLE_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=TOP_N_WORDS)
