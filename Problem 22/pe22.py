"""
This program has been written to solve problem 21 on projecteuler.net
author: Jeremiah Lantzer
"""

import time


def import_text_file():
    text = open("p022_names.txt", "r").read()
    return text


def create_names_list():
    text = import_text_file().replace('"', '')
    name_list = text.split(",")
    name_list = sorted(name_list)
    return name_list


def sum_of_each_name(names_list):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum_list = []

    for name in names_list:
        sum = 0
        for letter in name:
            sum += (alphabet.find(letter) + 1)
        sum_list.append(sum)
    return sum_list


def func():
    names_list = create_names_list()
    sum_of_names_list = sum_of_each_name(names_list)
    score_sum = 0

    for indx, name_sum in enumerate(sum_of_names_list):
        score_sum += ((indx + 1) * name_sum)
        print(indx + 1, name_sum, names_list[indx])

    return score_sum


start = time.time()
result = func()
elapsed = time.time() - start

print("\nResult: %s \nFound in %s seconds" % (result, elapsed))
