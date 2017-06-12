from flask import Blueprint, render_template

from constants import (ABC_BASE,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from query_functions import MONTHS, THIS, LAST, NEXT
from trending_words import trends


abc = Blueprint("abc", __name__)


@abc.route('/today')
def abc_today():
    title = 'ABC Australia - Top words today'
    main_data = {**ABC_BASE, **{"data": data("abc", "ondate", "today")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("abc", "day_on_day")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@abc.route('/week')
def abc_week():
    title = 'ABC Australia - Top words this week'
    main_data = {**ABC_BASE, **{"data": data("abc", "since", "week")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("abc", "week_on_week")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@abc.route('/month')
def abc_month():
    title = 'ABC Australia - Top words this month'
    main_data = {**ABC_BASE, **{"data": data("abc", "since", "month")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("abc", "month_on_month")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@abc.route('/ever')
def abc_ever():
    title = 'ABC Australia - Top words ever'
    main_data = {**ABC_BASE, **{"data": data("abc", "ever")}}
    extra_data_1 = {"title": MONTHS[LAST]["name"],
                    "data": data("abc", "between", MONTHS[LAST]["start"],
                                                   MONTHS[THIS]["start"])}
    extra_data_2 = {"title": MONTHS[THIS]["name"],
                    "data": data("abc", "between", MONTHS[THIS]["start"],
                                                   MONTHS[NEXT]["start"])}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=DOUBLE_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=TOP_N_WORDS)
