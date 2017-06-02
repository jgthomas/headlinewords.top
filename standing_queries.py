

from query import data

from trending_words import trends


## BASE DATA ##
BBC_BASE = {"source": "bbc", "title": "BBC"}
NYT_BASE = {"source": "nyt", "title": "New York Times"}
DML_BASE = {"source": "dml", "title": "Daily Mail"}
FOX_BASE = {"source": "fox", "title": "Fox News"}


## TIME PERIODS ##
BBC_TODAY = {**BBC_BASE, **{"data": data("bbc", "ondate", "today")}}
BBC_WEEK = {**BBC_BASE, **{"data": data("bbc", "since", "week")}}
BBC_MONTH = {**BBC_BASE, **{"data": data("bbc", "since", "month")}}
BBC_EVER = {**BBC_BASE, **{"data": data("bbc", "ever")}}

NYT_TODAY = {**NYT_BASE, **{"data": data("nyt", "ondate", "today")}}
NYT_WEEK = {**NYT_BASE, **{"data": data("nyt", "since", "week")}}
NYT_MONTH = {**NYT_BASE, **{"data": data("nyt", "since", "month")}}
NYT_EVER = {**NYT_BASE, **{"data": data("nyt", "ever")}}

DML_TODAY = {**DML_BASE, **{"data": data("dml", "ondate", "today")}}
DML_WEEK = {**DML_BASE, **{"data": data("dml", "since", "week")}}
DML_MONTH = {**DML_BASE, **{"data": data("dml", "since", "month")}}
DML_EVER = {**DML_BASE, **{"data": data("dml", "ever")}}

FOX_TODAY = {**FOX_BASE, **{"data": data("fox", "ondate", "today")}}
FOX_WEEK = {**FOX_BASE, **{"data": data("fox", "since", "week")}}
FOX_MONTH = {**FOX_BASE, **{"data": data("fox", "since", "month")}}
FOX_EVER = {**FOX_BASE, **{"data": data("fox", "ever")}}


## MONTHS
# Base
MAY_BASE = {"title": "May"}
JUN_BASE = {"title": "June"}
# Sources
BBC_MAY = {**MAY_BASE, **{"data": data("bbc", "between", "may_start", "jun_start")}}
BBC_JUN = {**JUN_BASE, **{"data": data("bbc", "between", "jun_start", "jul_start")}}

NYT_MAY = {**MAY_BASE, **{"data": data("nyt", "between", "may_start", "jun_start")}}
NYT_JUN = {**JUN_BASE, **{"data": data("nyt", "between", "jun_start", "jul_start")}}


## TRENDING
# Base
RISING_BASE = {"title": "Rising"}
FALLING_BASE = {"title": "Falling"}
# Sources
BBC_TODAY_RISING = {**RISING_BASE}
BBC_TODAY_FALLING  = {**FALLING_BASE}
BBC_TODAY_RISING["data"], BBC_TODAY_FALLING["data"] = trends("bbc", "day_on_day")

BBC_WEEK_RISING = {**RISING_BASE}
BBC_WEEK_FALLING  = {**FALLING_BASE}
BBC_WEEK_RISING["data"], BBC_WEEK_FALLING["data"] = trends("bbc", "week_on_week")

NYT_TODAY_RISING = {**RISING_BASE}
NYT_TODAY_FALLING  = {**FALLING_BASE}
NYT_TODAY_RISING["data"], NYT_TODAY_FALLING["data"] = trends("nyt", "day_on_day")

NYT_WEEK_RISING = {**RISING_BASE}
NYT_WEEK_FALLING  = {**FALLING_BASE}
NYT_WEEK_RISING["data"], NYT_WEEK_FALLING["data"] = trends("nyt", "week_on_week")

DML_TODAY_RISING = {**RISING_BASE}
DML_TODAY_FALLING  = {**FALLING_BASE}
DML_TODAY_RISING["data"], DML_TODAY_FALLING["data"] = trends("dml", "day_on_day")

FOX_TODAY_RISING = {**RISING_BASE}
FOX_TODAY_FALLING  = {**FALLING_BASE}
FOX_TODAY_RISING["data"], FOX_TODAY_FALLING["data"] = trends("fox", "day_on_day")
