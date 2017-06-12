from flask import Blueprint, render_template

from constants import (UK_BASE, US_BASE, AU_BASE,
                       UK_SOURCES, US_SOURCES, AU_SOURCES,
                       DOUBLE_N_WORDS)

from query import data
from composite_counts import composite_ranks


by_country = Blueprint("by_country", __name__)


@by_country.route('/today')
def country_day():
    title = 'By Country - Today'
    page_title = "Country Comparison"
    uk_sources = [data(source, 'ondate', 'today') for source in UK_SOURCES]
    us_sources = [data(source, 'ondate', 'today') for source in US_SOURCES]
    au_sources = [data(source, 'ondate', 'today') for source in AU_SOURCES]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    au_combined = {**AU_BASE, **{"data": composite_ranks(au_sources)}}
    return render_template('combined.html',
                           page_title=page_title,
                           title=title,
                           sources=(uk_combined,
                                    us_combined,
                                    au_combined),
                           display=DOUBLE_N_WORDS)


@by_country.route('/week')
def country_week():
    title = 'By Country - This Week'
    page_title = "Country Comparison"
    uk_sources = [data(source, 'since', 'week') for source in UK_SOURCES]
    us_sources = [data(source, 'since', 'week') for source in US_SOURCES]
    au_sources = [data(source, 'since', 'week') for source in AU_SOURCES]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    au_combined = {**AU_BASE, **{"data": composite_ranks(au_sources)}}
    return render_template('combined.html',
                           page_title=page_title,
                           title=title,
                           sources=(uk_combined,
                                    us_combined,
                                    au_combined),
                           display=DOUBLE_N_WORDS)


@by_country.route('/month')
def country_month():
    title = 'By Country - This Month'
    page_title = "Country Comparison"
    uk_sources = [data(source, 'since', 'month') for source in UK_SOURCES]
    us_sources = [data(source, 'since', 'month') for source in US_SOURCES]
    au_sources = [data(source, 'since', 'month') for source in AU_SOURCES]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    au_combined = {**AU_BASE, **{"data": composite_ranks(au_sources)}}
    return render_template('combined.html',
                           page_title=page_title,
                           title=title,
                           sources=(uk_combined,
                                    us_combined,
                                    au_combined),
                           display=DOUBLE_N_WORDS)


@by_country.route('/ever')
def country_ever():
    title = 'By Country - Ever'
    page_title = "Country Comparison"
    uk_sources = [data(source, 'ever') for source in UK_SOURCES]
    us_sources = [data(source, 'ever') for source in US_SOURCES]
    au_sources = [data(source, 'ever') for source in AU_SOURCES]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    au_combined = {**AU_BASE, **{"data": composite_ranks(au_sources)}}
    return render_template('combined.html',
                           page_title=page_title,
                           title=title,
                           sources=(uk_combined,
                                    us_combined,
                                    au_combined),
                           display=DOUBLE_N_WORDS)
