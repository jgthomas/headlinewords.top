from flask import Blueprint, render_template

from constants import (NYT_BASE,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from trending_words import trends
from graph import get_plot


nyt = Blueprint("nyt", __name__)


@nyt.route('/today')
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
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS,
                           plots=(plot_1, plot_2))


@nyt.route('/week')
def nyt_week():
    title = 'New York Times - Top words this week'
    main_data = {**NYT_BASE, **{"data": data("nyt", "since", "week")}}
    extra_data_1 = {"title": "Rising"}
    extra_data_2 = {"title": "Falling"}
    extra_data_1["data"], extra_data_2["data"] = trends("nyt", "week_on_week")
    plot_1 = get_plot(title="Top five progress",
                      filename="nyt_week_1.png")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display= SHORT_N_WORDS,
                           plots=(plot_1,))


@nyt.route('/month')
def nyt_month():
    title = 'New York Times - Top words this month'
    main_data = {**NYT_BASE, **{"data": data("nyt", "since", "month")}}
    plot_1 = get_plot(title="Top five progress",
                      filename="nyt_month_1.png")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           plots=(plot_1,))


@nyt.route('/ever')
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
                           title=title,
                           source=main_data,
                           display=DOUBLE_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=TOP_N_WORDS,
                           plots=(plot_1,))
