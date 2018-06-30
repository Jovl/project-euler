"""
This program has been written to solve problem 19 on projecteuler.net
author: Jeremiah Lantzer
"""

import time
from datetime import date
from collections import Counter

start_year = 1901
end_year = 2000
start_month = 1
end_month = 12
counter = Counter()


def count_sundays():
    for year in range(start_year, end_year + 1):
        for month in range(start_month, end_month + 1):
            day = date(year, month, 1)
            counter[day.weekday()] += 1

    return counter[6]


start = time.time()
result = count_sundays()
elapsed = time.time() - start

print("\nResult: %s \nFound in %s seconds" % (result, elapsed))
