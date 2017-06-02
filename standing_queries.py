

from query import data

from trending_words import trends


## BASE DATA
BBC_BASE = {"source": "bbc", "title": "BBC"}
NYT_BASE = {"source": "nyt", "title": "New York Times"}


## TIME PERIODS
BBC_TODAY = {**BBC_BASE, **{"data": data("bbc", "ondate", "today")}}
BBC_WEEK = {**BBC_BASE, **{"data": data("bbc", "since", "week")}}
BBC_MONTH = {**BBC_BASE, **{"data": data("bbc", "since", "month")}}
BBC_EVER = {**BBC_BASE, **{"data": data("bbc", "ever")}}

NYT_TODAY = {**NYT_BASE, **{"data": data("nyt", "ondate", "today")}}
NYT_WEEK = {**NYT_BASE, **{"data": data("nyt", "since", "week")}}
NYT_MONTH = {**NYT_BASE, **{"data": data("nyt", "since", "month")}}
NYT_EVER = {**NYT_BASE, **{"data": data("nyt", "ever")}}


## TRENDING
BBC_TODAY_RISING = {"title": "Rising"}
BBC_TODAY_FALLING = {"title": "Falling"}
BBC_TODAY_RISING["data"], BBC_TODAY_FALLING["data"] = trends("bbc", "day_on_day")

BBC_WEEK_RISING = {"title": "Rising"}
BBC_WEEK_FALLING = {"title": "Falling"}
BBC_WEEK_RISING["data"], BBC_WEEK_FALLING["data"] = trends("bbc", "week_on_week")

#BBC_MONTH_RISING = {"title": "Rising"}
#BBC_MONTH_FALLING = {"title": "Falling"}
#BBC_MONTH_RISING["data"], BBC_MONTH_FALLING["data"] = trends("bbc", "month_on_month")

NYT_TODAY_RISING = {"title": "Rising"}
NYT_TODAY_FALLING = {"title": "Falling"}
NYT_TODAY_RISING["data"], NYT_TODAY_FALLING["data"] = trends("nyt", "day_on_day")

NYT_WEEK_RISING = {"title": "Rising"}
NYT_WEEK_FALLING = {"title": "Falling"}
NYT_WEEK_RISING["data"], NYT_WEEK_FALLING["data"] = trends("nyt", "week_on_week")

#NYT_MONTH_RISING = {"title": "Rising"}
#NYT_MONTH_FALLING = {"title": "Falling"}
#NYT_MONTH_RISING["data"], NYT_MONTH_FALLING["data"] = trends("nyt", "month_on_month")
