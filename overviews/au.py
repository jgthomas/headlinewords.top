from flask import Blueprint, render_template

from constants import (AU_SOURCES,
                       AU_BASE,
                       SHORT_N_WORDS,
                       TOP_N_WORDS,
                       DOUBLE_N_WORDS)

from query import data
from query_functions import MONTHS, THIS, LAST, NEXT
from trending_words import trends
from composite_counts import composite_ranks


au = Blueprint("au", __name__)


@au.route('/today')
def au_today():
    title = 'Top words in Australia today'
    au_today = [data(source, "ondate", "today") for source in AU_SOURCES]
    au_combined = {**AU_BASE, "data": composite_ranks(au_today)}
    day_up, day_down = zip(*[trends(source, "day_on_day")
                             for source in AU_SOURCES])
    rising = {"title": "Rising", "data": composite_ranks(day_up)}
    falling = {"title": "Falling", "data": composite_ranks(day_down, rev=False)}
    return render_template('source.html',
                           title=title,
                           source=au_combined,
                           display=TOP_N_WORDS,
                           extras=(rising, falling),
                           extra_display=SHORT_N_WORDS)


@au.route('/week')
def au_week():
    title = 'Top words in Australia this week'
    au_week = [data(source, "since", "week") for source in AU_SOURCES]
    au_combined = {**AU_BASE, "data": composite_ranks(au_week)}
    week_up, week_down = zip(*[trends(source, "week_on_week")
                               for source in AU_SOURCES])
    rising = {"title": "Rising", "data": composite_ranks(week_up)}
    falling = {"title": "Falling", "data": composite_ranks(week_down, rev=False)}
    return render_template('source.html',
                           title=title,
                           source=au_combined,
                           display=TOP_N_WORDS,
                           extras=(rising, falling),
                           extra_display=SHORT_N_WORDS)
                           

@au.route('/month')
def au_month():
    title = 'Top words in Australia this month'
    au_month = [data(source, "since", "month") for source in AU_SOURCES]
    au_combined = {**AU_BASE, "data": composite_ranks(au_month)}
    month_up, month_down = zip(*[trends(source, "month_on_month")
                                 for source in AU_SOURCES])
    rising = {"title": "Rising", "data": composite_ranks(month_up)}
    falling = {"title": "Falling", "data": composite_ranks(month_down, rev=False)}
    return render_template('source.html',
                           title=title,
                           source=au_combined,
                           display=TOP_N_WORDS,
                           extras=(rising, falling),
                           extra_display=SHORT_N_WORDS)


@au.route('/ever')
def au_ever():
    title = 'Top words in Australia ever'
    au_ever = [data(source, "ever") for source in AU_SOURCES]
    au_combined = {**AU_BASE, "data": composite_ranks(au_ever)}
    last = [data(source, "between", MONTHS[LAST]["start"], MONTHS[THIS]["start"])
            for source in AU_SOURCES]
    this = [data(source, "between", MONTHS[THIS]["start"], MONTHS[NEXT]["start"])
            for source in AU_SOURCES]
    last_month = {"title": MONTHS[LAST]["name"],
                  "data": composite_ranks(last)}
    this_month = {"title": MONTHS[THIS]["name"],
                  "data": composite_ranks(this)}
    return render_template('source.html',
                           title=title,
                           source=au_combined,
                           display=DOUBLE_N_WORDS,
                           extras=(last_month, this_month),
                           extra_display=TOP_N_WORDS)
