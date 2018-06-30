"""
This program has been written to solve problem 5 on projecteuler.net
author: Jeremiah Lantzer
"""

import sys

divis_digits = 20   # The final number must be divisible by 1...10
not_found = True    # used to run the loop iterating the process
counter = 2520      # starting from this number which is divisible by all numbers 1...10
count_check = 0     # if this number = divis_digits the number has been found

while not_found and counter < sys.maxsize:
    counter += divis_digits
    # print(counter)

    for i in range(1, divis_digits + 1):
        if counter % i == 0:
            count_check += 1
        else:
            count_check = 0
            break

    if count_check == divis_digits:
        not_found = False
        print("Final Number: " + str(counter))
