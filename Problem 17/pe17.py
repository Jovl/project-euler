"""
This program has been written to solve problem 17 on projecteuler.net
author: Jeremiah Lantzer
"""

import time

limiting_num = 1000


def letter_count(limit):
    total = 0

    numbers = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
               10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
               17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
               60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "thousand"}

    for i in range(1, limit + 1):
        if i <= 20:
            print(numbers[i])
            total += len(numbers[i])

        elif 20 < i < 100:
            i_str1 = str(i)
            first_digit1 = int(i_str1[0] + "0")
            second_digit1 = int(i_str1[1])
            print(numbers[first_digit1], numbers[second_digit1])
            total += (len(numbers[first_digit1]) + len(numbers[second_digit1]))

        elif 100 <= i < 1000:
            i_str2 = str(i)
            first_digit2 = int(i_str2[0])
            second_digit2 = int(i_str2[1] + "0")
            third_digit = int(i_str2[2])

            if third_digit == 0 and second_digit2 == 0:
                total += (len(numbers[first_digit2]) + len(numbers[100]))
            else:
                if int(i_str2[1:]) <= 20:
                    print(numbers[first_digit2], numbers[100], "and", numbers[int(i_str2[1:])])
                    total += (len(numbers[first_digit2]) + len(numbers[100]) + len("and") + len(numbers[int(i_str2[1:])]))
                else:
                    print(numbers[first_digit2], numbers[100], "and", numbers[second_digit2], numbers[third_digit])
                    total += (len(numbers[first_digit2]) + len(numbers[100]) + len("and") + len(numbers[second_digit2]) + len(numbers[third_digit]))

        elif i == 1000:
            print(numbers[1], numbers[1000])
            total += (len(numbers[1]) + len(numbers[1000]))

    return total


start = time.time()
result = letter_count(limiting_num)
elapsed = time.time() - start

print("\nResult: %s \nFound in %s seconds" % (result, elapsed))
