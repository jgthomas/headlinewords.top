

from query import data
from trending_words import trends


## TIME PERIODS
BBC_TODAY = {"title": "BBC",
             "data": data("bbc", "ondate", "today")}

BBC_WEEK = {"title": "BBC",
            "data": data("bbc", "since", "week")}

BBC_MONTH = {"title": "BBC",
             "data": data("bbc", "since", "month")}

BBC_EVER = {"title": "BBC",
            "data": data("bbc", "ever")}

NYT_TODAY = {"title": "New York Times",
             "data": data("nyt", "ondate", "today")}

NYT_WEEK = {"title": "New York Times",
            "data": data("nyt", "since", "week")}

NYT_MONTH = {"title": "New York Times",
             "data": data("nyt", "since", "month")}

NYT_EVER = {"title": "New York Times",
            "data": data("nyt", "ever")}


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
