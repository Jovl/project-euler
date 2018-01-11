"""
This program has been written to solve problem 18 on projecteuler.net
author: Jeremiah Lantzer
"""

import time

filename = "input.txt"


def max_path_sum(file):
    input_lines = input_data(file)
    print(input_lines)
    highest_values = []
    highest_value = 0
    prev_idx = 0

    for line in input_lines:
        for idx, val in enumerate(line):
            if int(val) > highest_value and (idx == prev_idx or idx == prev_idx + 1):
                highest_value = int(val)
                prev_idx = idx
        highest_values.append(highest_value)
        highest_value = 0
        prev_idx = 0

    print(highest_values)

    total = sum(highest_values)
    return total


def input_data(fname):
    input_lines = []
    with open(fname) as f:
        for line in f:
            input_lines.append(line.strip().split(' '))
    return input_lines


start = time.time()
result = max_path_sum(filename)
elapsed = time.time() - start

print("\nResult: %s \nFound in %s seconds" % (result, elapsed))
