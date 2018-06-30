"""
This program has been written to solve problem 9 on projecteuler.net
author: Jeremiah Lantzer
"""

import math

limit = 1000
triplet_ansr = 0


def is_square(num):
    root = math.sqrt(num)
    if int(root + 0.5) ** 2 == num:
        return True
    else:
        return False

for i in range(1, limit):
    for j in range(1, limit):
        if i < j:
            triplet_ansr = math.pow(i, 2) + math.pow(j, 2)

        if is_square(triplet_ansr):
            k = math.sqrt(triplet_ansr)
            if i + j + k == limit:
                print("A: ", i)
                print("B: ", j)
                print("C: ", k)
                print("Answer: ", i*j*k)
