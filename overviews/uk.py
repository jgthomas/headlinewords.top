from flask import Blueprint, render_template

from constants import (UK_SOURCES,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from query_functions import TODAY, MONTHS
from trending_words import trends
from composite_counts import composite_ranks


uk = Blueprint("uk", __name__)


@uk.route('/today')
def uk_today():
    title = 'Top words in UK today'
    uk_today = [data(source, "ondate", "today") for source in UK_SOURCES]
    uk_combined = {"source": "uk",
                   "title": "UK",
                   "data": composite_ranks(uk_today)}
    day_up, day_down = zip(*[trends(source, "day_on_day")
                             for source in UK_SOURCES])
    rising = {"title": "Rising", "data": composite_ranks(day_up)}
    falling = {"title": "Falling", "data": composite_ranks(day_down, rev=False)}
    return render_template('source.html',
                           title=title,
                           source=uk_combined,
                           display=TOP_N_WORDS,
                           extras=(rising, falling),
                           extra_display=SHORT_N_WORDS)


@uk.route('/week')
def uk_week():
    title = 'Top words in UK this week'
    uk_week = [data(source, "since", "week") for source in UK_SOURCES]
    uk_combined = {"source": "uk",
                   "title": "UK",
                   "data": composite_ranks(uk_week)}
    week_up, week_down = zip(*[trends(source, "week_on_week")
                               for source in UK_SOURCES])
    rising = {"title": "Rising", "data": composite_ranks(week_up)}
    falling = {"title": "Falling", "data": composite_ranks(week_down, rev=False)}
    return render_template('source.html',
                           title=title,
                           source=uk_combined,
                           display=TOP_N_WORDS,
                           extras=(rising, falling),
                           extra_display=SHORT_N_WORDS)
                           

@uk.route('/month')
def uk_month():
    title = 'Top words in UK this month'
    uk_month = [data(source, "since", "month") for source in UK_SOURCES]
    uk_combined = {"source": "uk",
                   "title": "UK",
                   "data": composite_ranks(uk_month)}
    month_up, month_down = zip(*[trends(source, "month_on_month")
                                 for source in UK_SOURCES])
    rising = {"title": "Rising", "data": composite_ranks(month_up)}
    falling = {"title": "Falling", "data": composite_ranks(month_down, rev=False)}
    return render_template('source.html',
                           title=title,
                           source=uk_combined,
                           display=TOP_N_WORDS,
                           extras=(rising, falling),
                           extra_display=SHORT_N_WORDS)


@uk.route('/ever')
def uk_ever():
    THIS = TODAY.month
    LAST = THIS - 1
    NEXT = THIS + 1
    title = 'Top words in UK ever'
    uk_ever = [data(source, "ever") for source in UK_SOURCES]
    uk_combined = {"source": "uk",
                   "title": "UK",
                   "data": composite_ranks(uk_ever)}
    last = [data(source, "between", MONTHS[LAST]["start"], MONTHS[THIS]["start"])
            for source in UK_SOURCES]
    this = [data(source, "between", MONTHS[THIS]["start"], MONTHS[NEXT]["start"])
            for source in UK_SOURCES]
    last_month = {"title": MONTHS[LAST]["name"],
                  "data": composite_ranks(last)}
    this_month = {"title": MONTHS[THIS]["name"],
                  "data": composite_ranks(this)}
    return render_template('source.html',
                           title=title,
                           source=uk_combined,
                           display=DOUBLE_N_WORDS,
                           extras=(last_month, this_month),
                           extra_display=TOP_N_WORDS)
