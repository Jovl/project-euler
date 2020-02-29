"""
This program has been written to solve problem 23 on projecteuler.net
author: Jeremiah Lantzer
"""

import time
import math


def divisorGen(num):
    divs = [1]
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divs.extend([i, num / i])
    return list(set(divs))


def determineAbundance(initialNum, divisors):
    divSum = sum(divisors)

    if divSum > initialNum:
        return initialNum

    return None


def func():
    abundants = []

    for i in range(12, 28124):
        print(i)
        if sum(divisorGen(i)) > i:
            print(divisorGen(i))
            abundants.append(i)

    nonAbundantNums = [x for x in range(28124)]

    for i in range(len(abundants)):
        for j in range(i, 28124):
            if abundants[i] + abundants[j] < 28124:
                # negating the value of the abundant sum
                nonAbundantNums[abundants[i] + nonAbundantNums[j]] = 0
            else:
                break

    return sum(nonAbundantNums)


start = time.time()
result = func()
elapsed = time.time() - start

print("\nResult: %s \nFound in %s seconds" % (result, elapsed))