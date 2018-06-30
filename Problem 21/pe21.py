"""
This program has been written to solve problem 21 on projecteuler.net
author: Jeremiah Lantzer
"""

import time


def find_divisors_of_one_num(num):
    num_list = []
    i = 1
    while i < num:
        if num % i == 0:
            num_list.append(i)
        i = i + 1
    return num_list


def sum_divisors_results(num):
    sum_list = find_divisors_of_one_num(num)
    sum_list = sum(sum_list)
    return sum_list


def amicable_pairs(max_num):
    divisors_sum_list = []
    amicables_list = []
    amicable_sum = 0
    for i in range(1, max_num + 1):
        divisors_sum_list.append(sum_divisors_results(i))

    for indx, num in enumerate(divisors_sum_list):
        if num <= max_num:
            if indx + 1 == divisors_sum_list[num - 1] and indx + 1 != num:
                amicables_list.append(indx + 1)
                print(indx + 1, num)
    print(amicables_list)
    print(divisors_sum_list[219])
    print(divisors_sum_list[283])

    return sum(amicables_list)


start = time.time()
result = amicable_pairs(10000)
elapsed = time.time() - start

print("\nResult: %s \nFound in %s seconds" % (result, elapsed))
