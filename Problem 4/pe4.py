"""
This program has been written to solve problem 4 on projecteuler.net
author: Jeremiah Lantzer
"""

start_num = 999
end_num = 100


def reverse(string):
    return string[::-1]

for i in range(start_num, end_num, -1):
    for j in range(start_num, end_num, -1):
        product = i * j
        product_str = str(product)
        if product_str == reverse(product_str):
            print(product)
