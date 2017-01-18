"""
This program has been written to solve problem 14 on projecteuler.net
author: Jeremiah Lantzer
"""


def even_formula(n):
    return n / 2


def odd_formula(n):
    return 3 * n + 1


def next_step(n):
    if n % 2 == 0:
        step = even_formula(n)
        return next_step(step)
    elif n == 1:
        return 1
    else:
        step = odd_formula(n)
        return next_step(step)

starting_number = 1000000
dynamic_condition = 0
check = 0
chain = []

while starting_number > dynamic_condition:
    starting_number -= 1
    while check != 1:
        check = next_step(starting_number)
