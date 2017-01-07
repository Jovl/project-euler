"""
This program has been written to solve problem 3 on projecteuler.net
author: Jeremiah Lantzer
"""

import math

max_num = 600851475143
prime_factors = []


def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

for i in range(2, max_num):
    if is_prime(i) and max_num % i == 0:
        prime_factors.append(i)
        print(i)

print(prime_factors)
