from flask import Blueprint, render_template

from constants import (UK_BASE, US_BASE, AU_BASE,
                       DOUBLE_N_WORDS)

from query import data
from composite_counts import composite_ranks


by_country = Blueprint("by_country", __name__)


@by_country.route('/today')
def country_day():
    title = 'By Country - Today'
    page_title = "Country Comparison"
    uk_sources = [data('bbc', 'ondate', 'today'),
                  data('dml', 'ondate', 'today')]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_sources = [data('nyt', 'ondate', 'today'),
                  data('fox', 'ondate', 'today')]
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    au_sources = [data('smh', 'ondate', 'today'),
                  data('abc', 'ondate', 'today')]
    au_combined = {**AU_BASE, **{"data": composite_ranks(au_sources)}}
    return render_template('combined.html',
                           page_title = page_title,
                           title = title,
                           sources = (uk_combined,
                                      us_combined,
                                      au_combined),
                           display = DOUBLE_N_WORDS)

@by_country.route('/week')
def country_week():
    title = 'By Country - This Week'
    page_title = "Country Comparison"
    uk_sources = [data('bbc', 'since', 'week'),
                  data('dml', 'since', 'week')]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_sources = [data('nyt', 'since', 'week'),
                  data('fox', 'since', 'week')]
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    au_sources = [data('smh', 'since', 'week'),
                  data('abc', 'since', 'week')]
    au_combined = {**AU_BASE, **{"data": composite_ranks(au_sources)}}
    return render_template('combined.html',
                           page_title = page_title,
                           title = title,
                           sources = (uk_combined,
                                      us_combined,
                                      au_combined),
                           display = DOUBLE_N_WORDS)

@by_country.route('/month')
def country_month():
    title = 'By Country - This Month'
    page_title = "Country Comparison"
    uk_sources = [data('bbc', 'since', 'month'),
                  data('dml', 'since', 'month')]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_sources = [data('nyt', 'since', 'month'),
                  data('fox', 'since', 'month')]
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    au_sources = [data('smh', 'since', 'month'),
                  data('abc', 'since', 'month')]
    au_combined = {**AU_BASE, **{"data": composite_ranks(au_sources)}}
    return render_template('combined.html',
                           page_title = page_title,
                           title = title,
                           sources = (uk_combined,
                                      us_combined,
                                      au_combined),
                           display = DOUBLE_N_WORDS)

@by_country.route('/ever')
def country_ever():
    title = 'By Country - Ever'
    page_title = "Country Comparison"
    uk_sources = [data('bbc', 'ever'),
                  data('dml', 'ever')]
    uk_combined = {**UK_BASE, **{"data": composite_ranks(uk_sources)}}
    us_sources = [data('nyt', 'ever'),
                  data('fox', 'ever')]
    us_combined = {**US_BASE, **{"data": composite_ranks(us_sources)}}
    au_sources = [data('smh', 'ever'),
                  data('abc', 'ever')]
    au_combined = {**AU_BASE, **{"data": composite_ranks(au_sources)}}
    return render_template('combined.html',
                           page_title = page_title,
                           title = title,
                           sources = (uk_combined,
                                      us_combined,
                                      au_combined),
                           display = DOUBLE_N_WORDS)
