"""
This program has been written to solve problem 14 on projecteuler.net
author: Jeremiah Lantzer
"""

import sys
sys.setrecursionlimit(3500)
print(sys.getrecursionlimit())


def even_formula(n):
    return n / 2


def odd_formula(n):
    return 3 * n + 1


def next_step(n, chain):
    if n % 2 == 0:
        step = even_formula(n)
        chain.append(step)
        return next_step(step, chain)
    elif n == 1:
        chain.append(1)
        return 1
    else:
        step = odd_formula(n)
        chain.append(step)
        return next_step(step, chain)

starting_number = 1000000
base = 0
check = 0
stored = 0
chain = []

while starting_number > base:
    starting_number -= 1
    # print("Starting Number: ", starting_number)
    chain.append(starting_number)
    next_step(starting_number, chain)
    temp = len(chain)
    # print("Length: ", temp)

    if temp > stored:
        temp_start = starting_number
        stored = temp
        print("Final: ", stored, temp_start)

    chain.clear()
