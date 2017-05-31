

from query import data


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
