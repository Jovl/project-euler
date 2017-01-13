"""
This program has been written to solve problem 7 on projecteuler.net
author: Jeremiah Lantzer
"""

import math

prime_wanted = 10001    # need to find the 10001st prime number
current_prime = 13      # given that 13 is the 6th prime number
prime_counter = 6


def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

while prime_counter < prime_wanted:
    current_prime += 1
    if is_prime(current_prime):
        prime_counter += 1

print(prime_counter)
print("10001st prime is: " + str(current_prime))
