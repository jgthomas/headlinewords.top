
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

CALENDAR_MAP = {"jan_start": dt.datetime(THIS_YEAR - 1, 12, 31),
                "jan_end": dt.datetime(THIS_YEAR, 2, 1),
                "feb_start": dt.datetime(THIS_YEAR, 1, 31),
                "feb_end": dt.datetime(THIS_YEAR, 3, 1),
                "mar_start": dt.datetime(THIS_YEAR, 2, 28),
                "mar_end": dt.datetime(THIS_YEAR, 4, 1),
                "apr_start": dt.datetime(THIS_YEAR, 3, 31),
                "apr_end": dt.datetime(THIS_YEAR, 5, 1),
                "may_start": dt.datetime(THIS_YEAR, 4, 30),
                "may_end": dt.datetime(THIS_YEAR, 6, 1),
                "jun_start": dt.datetime(THIS_YEAR, 5, 31),
                "jun_end": dt.datetime(THIS_YEAR, 7, 1),
                "jul_start": dt.datetime(THIS_YEAR, 6, 30),
                "jul_end": dt.datetime(THIS_YEAR, 8, 1),
                "aug_start": dt.datetime(THIS_YEAR, 7, 31),
                "aug_end": dt.datetime(THIS_YEAR, 9, 1),
                "sep_start": dt.datetime(THIS_YEAR, 8, 31),
                "sep_end": dt.datetime(THIS_YEAR, 10, 1),
                "oct_start": dt.datetime(THIS_YEAR, 9, 30),
                "oct_end": dt.datetime(THIS_YEAR, 11, 1),
                "nov_start": dt.datetime(THIS_YEAR, 10, 31),
                "nov_end": dt.datetime(THIS_YEAR, 12, 1),
                "dec_start": dt.datetime(THIS_YEAR, 11, 30),
                "dec_end": dt.datetime(THIS_YEAR + 1, 1, 1)}



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

    Ranges are *exclusive* when used for database queries.

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
    start = new_date(TOMORROW, days + 1)
    dates.append([start, end])
    num_periods -= 1
    while num_periods:
        end = new_date(start, 1, plus=True)
        start = new_date(start, days)
        dates.append([start, end])
        num_periods -= 1
    dates.reverse()
    return dates
