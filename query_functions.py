import datetime as dt


def new_date(start, num_days, plus=False):
    """ Return new date for num_days prior to (or after) start. """
    if plus:
        new_date = start + dt.timedelta(days=num_days)
    else:
        new_date = start - dt.timedelta(days=num_days)
    return new_date


TODAY = dt.datetime.today().date()
YESTERDAY = new_date(TODAY, 1)
TOMORROW = new_date(TODAY, 1, plus=True)

THIS_YEAR = TODAY.year

TIME_MAP = {"tomorrow": TOMORROW,
            "today": TODAY,
            "yesterday": YESTERDAY,
            "week": new_date(TODAY, 7),
            "month": new_date(TODAY, 30)}

CALENDAR_MAP = {"prev_dec": dt.datetime(THIS_YEAR - 1, 12, 1).date(),
                "jan_start": dt.datetime(THIS_YEAR, 1, 1).date(),
                "feb_start": dt.datetime(THIS_YEAR, 2, 1).date(),
                "mar_start": dt.datetime(THIS_YEAR, 3, 1).date(),
                "apr_start": dt.datetime(THIS_YEAR, 4, 1).date(),
                "may_start": dt.datetime(THIS_YEAR, 5, 1).date(),
                "jun_start": dt.datetime(THIS_YEAR, 6, 1).date(),
                "jul_start": dt.datetime(THIS_YEAR, 7, 1).date(),
                "aug_start": dt.datetime(THIS_YEAR, 8, 1).date(),
                "sep_start": dt.datetime(THIS_YEAR, 9, 1).date(),
                "oct_start": dt.datetime(THIS_YEAR, 10, 1).date(),
                "nov_start": dt.datetime(THIS_YEAR, 11, 1).date(),
                "dec_start": dt.datetime(THIS_YEAR, 12, 1).date(),
                "next_jan": dt.datetime(THIS_YEAR + 1, 1, 1).date()}


MONTHS = {0: {"start": "prev_dec", "name": "December"},
          1: {"start": "jan_start", "name": "January"},
          2: {"start": "feb_start", "name": "Feburary"},
          3: {"start": "mar_start", "name": "March"},
          4: {"start": "apr_start", "name": "April"},
          5: {"start": "may_start", "name": "May"},
          6: {"start": "jun_start", "name": "June"},
          7: {"start": "jul_start", "name": "July"},
          8: {"start": "aug_start", "name": "August"},
          9: {"start": "sep_start", "name": "September"},
          10: {"start": "oct_start", "name": "October"},
          11: {"start": "nov_start", "name": "November"},
          12: {"start": "dec_start", "name": "December"},
          13: {"start": "next_jan", "name": "January"}}

THIS = TODAY.month
LAST = THIS - 1
NEXT = THIS + 1

def date_of(year, month, day):
    """ Return date object for year, month and day. """
    return dt.datetime(year, month, day).date()


def date_range(start, days):
    """ Return range of consecutive date objects. """
    day_nums = [n for n in range(days, -1, -1)]
    return [new_date(start, n) for n in day_nums]


def strip_dates(data):
    stripped = []
    for word, count, *_ in data:
        stripped.append([word, count])
    return stripped


def just_words(data):
    words = []
    for word, *rest in data:
        words.append(word)
    return words


def date_spans(days, num_periods):
    """
    Return _num_periods_ pairs of date objects all _days_ apart.

    Ranges are run from midnight (i.e. the start) of the first day,
    to midnight (i.e the start) of the last day.

    Range is >= first date; < second date.

    Sequence of date-ranges returned reversed to aid graph plotting.

    Example: Date objects for two successive weeks
    >>> date_spans(7, 2)
    >>> [[datetime.date(2017, 5, 18), datetime.date(2017, 5, 26)],
         [datetime.date(2017, 5, 25), datetime.date(2017, 6, 2)]]

    Example: Date objects for two successive months
    >>> date_spans(30, 2)
    >>> [[datetime.date(2017, 4, 2), datetime.date(2017, 5, 3)],
         [datetime.date(2017, 5, 2), datetime.date(2017, 6, 2)]]

    """
    dates = []
    end = TOMORROW
    start = new_date(TOMORROW, days)
    dates.append([start, end])
    num_periods -= 1
    while num_periods:
        end = start
        start = new_date(start, days)
        dates.append([start, end])
        num_periods -= 1
    dates.reverse()
    return dates
