"""
This program has been written to solve problem 10 on projecteuler.net
author: Jeremiah Lantzer
"""

import math

max_num = 2000000
primes = []
primes_sum = 0


def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

for j in range(2, max_num + 1):
    if is_prime(j):
        primes.append(j)

for k in primes:
    primes_sum += k

print(primes_sum)
