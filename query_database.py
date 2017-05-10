#!/usr/bin/env python


import sqlite3


# Basic query strings
base = 'SELECT word, SUM(count), date as "[date]" FROM hw'
total = 'GROUP BY word ORDER BY SUM(count) DESC' 
date = 'WHERE "[date]"=?'
since = 'WHERE "[date]">?'
timespan = 'WHERE "[date]">? AND "[date]"<?'


# Compound query strings
overall_total = ' '.join([base, total])
specific_date = ' '.join([base, date, total])
since_date = ' '.join([base, since, total])
date_range = ' '.join([base, timespan, total])


def query(db, sql, opts=None):
    conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    with conn:
        if opts:
            cur.execute(sql, opts)
        else:
            cur.execute(sql)
        data = cur.fetchall()
    conn.close()
    return data


def main():
    with conn:
        print(query(overall_total))
    conn.close()


if __name__ == '__main__':

    main()
