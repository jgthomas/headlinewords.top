from flask import Blueprint, render_template

from constants import (HIT_BASE,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from query_functions import MONTHS, THIS, LAST, NEXT
from trending_words import trends


hit = Blueprint("hit", __name__)


@hit.route('/today')
def hit_today():
    title = 'Hindustan Times - Top words today'
    main_data = {**HIT_BASE, **{"data": data("hit", "ondate", "today")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("hit", "day_on_day")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@hit.route('/week')
def hit_week():
    title = 'Hindustan Times - Top words this week'
    main_data = {**HIT_BASE, **{"data": data("hit", "since", "week")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("hit", "week_on_week")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@hit.route('/month')
def hit_month():
    title = 'Hindustan Times - Top words this month'
    main_data = {**HIT_BASE, **{"data": data("hit", "since", "month")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("hit", "month_on_month")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@hit.route('/ever')
def hit_ever():
    title = 'Hindustan Times - Top words ever'
    main_data = {**HIT_BASE, **{"data": data("hit", "ever")}}
    extra_data_1 = {"title": MONTHS[LAST]["name"],
                    "data": data("hit", "between", MONTHS[LAST]["start"],
                                                   MONTHS[THIS]["start"])}
    extra_data_2 = {"title": MONTHS[THIS]["name"],
                    "data": data("hit", "between", MONTHS[THIS]["start"],
                                                   MONTHS[NEXT]["start"])}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=DOUBLE_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=TOP_N_WORDS)
