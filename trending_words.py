

from operator import itemgetter

from constants import BBC_DATABASE, NYT_DATABASE, TOP_N_WORDS, SHORT_N_WORDS

from query_database import (query, TODAY, TOMORROW, DATE_RANGE,
                            date_object_factory, just_words)

ONE_DAY = 1
WEEK_ON_WEEK = 7
MONTH_ON_MONTH = 30


def trim_data(data):
    trimmed = []
    for word, count, *_ in data:
        trimmed.append([word, count])
    return trimmed


def successive_periods(db, days):
    one_back = date_object_factory(TOMORROW, days + ONE_DAY)
    pivot = date_object_factory(one_back, ONE_DAY, plus=True)
    two_back = date_object_factory(one_back, days)
    this_period = query(db, DATE_RANGE, (one_back, TOMORROW))
    last_period = query(db, DATE_RANGE, (two_back, pivot))
    return (this_period, last_period)


def changing_counts(last_period, this_period):
    changes = []
    last = trim_data(last_period)
    this = trim_data(this_period)
    last_map = {word: count for word, count in last} 
    this_map = {word: count for word, count in this} 

    # Negative counts for words in last period but not this
    for key, value in last_map.items():
        temp = []
        if key not in this_map:
            temp.append(key)
            temp.append(value * -1)
        if temp:
            changes.append(temp)

    # Positive counts for new entries this period
    for key, value in this_map.items():
        temp = []
        if key not in last_map:
            temp.append(key)
            temp.append(value)
        else: # Change for words found in both periods
            temp.append(key)
            if this_map[key] > last_map[key]:
                temp.append(this_map[key] - last_map[key])
            elif last_map[key] > this_map[key]:
                temp.append(this_map[key] - last_map[key])
            else:
                temp.append(0)
        if temp:
            changes.append(temp)

    rising_words = [entry for entry in changes if entry[1] > 0]
    falling_words = [entry for entry in changes if entry[1] < 0] 
    rising_words.sort(key=itemgetter(1), reverse=True)
    falling_words.sort(key=itemgetter(1))
    return (rising_words, falling_words)


def main():
    this_week, last_week = successive_periods(BBC_DATABASE, WEEK_ON_WEEK)
    a, b = changing_counts(last_week, this_week)
    print(a)
    print(b)


if __name__ == '__main__':

    main()
