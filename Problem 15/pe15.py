"""
This program has been written to solve problem 15 on projecteuler.net
author: Jeremiah Lantzer
"""

import time

grid_size = 20


def find_paths(size):
    length = [1] * size

    for i in range(size):
        for j in range(i):
            length[j] = length[j] + length[j - 1]
        length[i] = 2 * length[i - 1]
    return length[size - 1]


start = time.time()
result = find_paths(grid_size)
elapsed = time.time() - start

print("\nResult: %s \nFound in %s seconds" % (result, elapsed))
