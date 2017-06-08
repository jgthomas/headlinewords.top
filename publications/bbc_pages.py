from flask import Blueprint, render_template

from constants import (BBC_BASE,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from trending_words import trends
from graph import get_plot


bbc = Blueprint("bbc", __name__)


@bbc.route('/today')
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
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS,
                           plots=(plot_1, plot_2))


@bbc.route('/week')
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
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=SHORT_N_WORDS,
                           plots=(plot_1, plot_2))


@bbc.route('/month')
def bbc_month():
    title = 'BBC - Top words this month'
    main_data = {**BBC_BASE, **{"data": data("bbc", "since", "month")}}
    plot_1 = get_plot(title="Top five progress",
                      filename="bbc_month_1.png")
    plot_2 = get_plot(title="The grimmest reaper",
                      filename="bbc_month_2.png")
    return render_template('source.html',
                           title=title,
                           source=main_data,
                           display=TOP_N_WORDS,
                           plots=(plot_1, plot_2))


@bbc.route('/ever')
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
                           title=title,
                           source=main_data,
                           display=DOUBLE_N_WORDS,
                           extras=(extra_data_1, extra_data_2),
                           extra_display=TOP_N_WORDS,
                           plots=(plot_1, plot_2))
