from flask import Blueprint, render_template

from constants import (IND_BASE,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from query_functions import MONTHS, THIS, LAST, NEXT
from trending_words import trends


ind = Blueprint("ind", __name__)


@ind.route('/today')
def ind_today():
    title = 'The Independent - Top words today'
    main_data = {**IND_BASE, **{"data": data("ind", "ondate", "today")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("ind", "day_on_day")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@ind.route('/week')
def ind_week():
    title = 'The Independent - Top words this week'
    main_data = {**IND_BASE, **{"data": data("ind", "since", "week")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("ind", "week_on_week")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@ind.route('/month')
def ind_month():
    title = 'The Independent - Top words this month'
    main_data = {**IND_BASE, **{"data": data("ind", "since", "month")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("ind", "month_on_month")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS)


@ind.route('/ever')
def ind_ever():
    title = 'The Independent - Top words ever'
    main_data = {**IND_BASE, **{"data": data("ind", "ever")}}
    extra_data_1 = {"title": MONTHS[LAST]["name"],
                    "data": data("ind", "between", MONTHS[LAST]["start"],
                                                   MONTHS[THIS]["start"])}
    extra_data_2 = {"title": MONTHS[THIS]["name"],
                    "data": data("ind", "between", MONTHS[THIS]["start"],
                                                   MONTHS[NEXT]["start"])}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=DOUBLE_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=TOP_N_WORDS)
