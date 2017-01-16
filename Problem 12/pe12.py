"""
This program has been written to solve problem 12 on projecteuler.net
author: Jeremiah Lantzer
"""

divisibles = 0
counter = 0


def tri_number(amount):
    triangle_number = 0
    for j in range(1, amount+1):
        triangle_number += j
    return triangle_number  # returns a certain triangle number given a positional number (1st, 2nd, 3rd)


while divisibles < 500:
    divisibles = 0
    counter += 1
    nat_sum = tri_number(counter)
    for i in range(1, nat_sum+1):
        if nat_sum % i == 0:
            divisibles += 1
    print("Amount of divisors for ", nat_sum, ": ", divisibles)

print(nat_sum)
