from flask import Blueprint, render_template

from constants import (US_SOURCES,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from query_functions import TODAY, MONTHS
from trending_words import trends
from composite_counts import composite_ranks


us = Blueprint("us", __name__)


@us.route('/today')
def us_today():
    title = 'Top words in USA today'
    us_today = [data(source, "ondate", "today") for source in US_SOURCES]
    us_combined = {"source": "us",
                   "title": "USA",
                   "data": composite_ranks(us_today)}
    day_up, day_down = zip(*[trends(source, "day_on_day")
                             for source in US_SOURCES])
    rising = {"title": "Rising", "data": composite_ranks(day_up)}
    falling = {"title": "Falling", "data": composite_ranks(day_down, rev=False)}
    return render_template('source.html',
                           title=title,
                           source=us_combined,
                           display=TOP_N_WORDS,
                           extras=(rising, falling),
                           extra_display=SHORT_N_WORDS)


@us.route('/week')
def us_week():
    title = 'Top words in USA this week'
    us_week = [data(source, "since", "week") for source in US_SOURCES]
    us_combined = {"source": "us",
                   "title": "USA",
                   "data": composite_ranks(us_week)}
    week_up, week_down = zip(*[trends(source, "week_on_week")
                               for source in US_SOURCES])
    rising = {"title": "Rising", "data": composite_ranks(week_up)}
    falling = {"title": "Falling", "data": composite_ranks(week_down, rev=False)}
    return render_template('source.html',
                           title=title,
                           source=us_combined,
                           display=TOP_N_WORDS,
                           extras=(rising, falling),
                           extra_display=SHORT_N_WORDS)
                           

@us.route('/month')
def us_month():
    title = 'Top words in USA this month'
    us_month = [data(source, "since", "month") for source in US_SOURCES]
    us_combined = {"source": "us",
                   "title": "USA",
                   "data": composite_ranks(us_month)}
    month_up, month_down = zip(*[trends(source, "month_on_month")
                                 for source in US_SOURCES])
    rising = {"title": "Rising", "data": composite_ranks(month_up)}
    falling = {"title": "Falling", "data": composite_ranks(month_down, rev=False)}
    return render_template('source.html',
                           title=title,
                           source=us_combined,
                           display=TOP_N_WORDS,
                           extras=(rising, falling),
                           extra_display=SHORT_N_WORDS)


@us.route('/ever')
def us_ever():
    THIS = TODAY.month
    LAST = THIS - 1
    NEXT = THIS + 1
    title = 'Top words in USA ever'
    us_ever = [data(source, "ever") for source in US_SOURCES]
    us_combined = {"source": "us",
                   "title": "USA",
                   "data": composite_ranks(us_ever)}
    last = [data(source, "between", MONTHS[LAST]["start"], MONTHS[THIS]["start"])
            for source in US_SOURCES]
    this = [data(source, "between", MONTHS[THIS]["start"], MONTHS[NEXT]["start"])
            for source in US_SOURCES]
    last_month = {"title": MONTHS[LAST]["name"],
                  "data": composite_ranks(last)}
    this_month = {"title": MONTHS[THIS]["name"],
                  "data": composite_ranks(this)}
    return render_template('source.html',
                           title=title,
                           source=us_combined,
                           display=DOUBLE_N_WORDS,
                           extras=(last_month, this_month),
                           extra_display=TOP_N_WORDS)
