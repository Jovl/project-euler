"""
This program has been written to solve problem 16 on projecteuler.net
author: Jeremiah Lantzer
"""

import time

exp = 1000
num = 2


def sum_of_digits(base, exponent):
    total = pow(base, exponent)
    sum = 0

    print("Exponential number: " + str(total))

    digits = [int(digit) for digit in str(total)]

    for num in digits:
        sum += num

    return sum


start = time.time()
result = sum_of_digits(num, exp)
elapsed = time.time() - start

print("\nResult: %s \nFound in %s seconds" % (result, elapsed))
