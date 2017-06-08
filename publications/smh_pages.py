from flask import Blueprint, render_template

from constants import (SMH_BASE,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data


smh = Blueprint("smh", __name__)


@smh.route('/today')
def smh_today():
    title = 'Sydney Morning Herald - Top words today'
    main_data = {**SMH_BASE, **{"data": data("smh", "ondate", "today")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS)


@smh.route('/week')
def smh_week():
    title = 'Sydney Morning Herald - Top words this week'
    main_data = {**SMH_BASE, **{"data": data("smh", "since", "week")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS)


@smh.route('/month')
def smh_month():
    title = 'Sydney Morning Herald - Top words this month'
    main_data = {**SMH_BASE, **{"data": data("smh", "since", "month")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS)


@smh.route('/ever')
def smh_ever():
    title = 'Sydney Morning Herald - Top words ever'
    main_data = {**SMH_BASE, **{"data": data("smh", "ever")}}
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=DOUBLE_N_WORDS)
