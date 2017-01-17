"""
This program has been written to solve problem 13 on projecteuler.net
author: Jeremiah Lantzer
"""

filename = 'pe13_input.txt'


def get_numbers(file):
    with open(file) as f:
        return[int(x) for x in f]


def sum_numbers(num_list):
    new_sum = 0
    for num in num_list:
        new_sum += num
    return str(new_sum)

nums = get_numbers(filename)
solution = str(sum_numbers(nums))
last_num = len(solution)
print("Unadjusted: ", solution)
print("Adjusted: ", solution[0:10])
