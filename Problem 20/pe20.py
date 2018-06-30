"""
This program has been written to solve problem 20 on projecteuler.net
author: Jeremiah Lantzer
"""

import time
import math


def sum_of_factorial_digits(num):
    factorial = math.factorial(num)
    factorial_string = str(factorial)
    factorial_sum = 0

    for num in factorial_string:
        factorial_sum += int(num)

    return factorial_sum


start = time.time()
result = sum_of_factorial_digits(100)
elapsed = time.time() - start

print("\nResult: %s \nFound in %s seconds" % (result, elapsed))
