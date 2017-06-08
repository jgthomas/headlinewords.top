from flask import Blueprint, render_template

from constants import (ABC_BASE,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data


abc = Blueprint("abc", __name__)


@abc.route('/today')
def abc_today():
    title = 'ABC Australia - Top words today'
    main_data = {**ABC_BASE, **{"data": data("abc", "ondate", "today")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS)

@abc.route('/week')
def abc_week():
    title = 'ABC Australia - Top words this week'
    main_data = {**ABC_BASE, **{"data": data("abc", "since", "week")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS)

@abc.route('/month')
def abc_month():
    title = 'ABC Australia - Top words this month'
    main_data = {**ABC_BASE, **{"data": data("abc", "since", "month")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS)

@abc.route('/ever')
def abc_ever():
    title = 'ABC Australia - Top words ever'
    main_data = {**ABC_BASE, **{"data": data("abc", "ever")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=DOUBLE_N_WORDS)
