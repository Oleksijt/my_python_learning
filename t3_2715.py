""" This Script is Task#3 in Programming_education course.
 The task is to calculate squares of numbers in range from
 0 to 100000000000.
 The code should be able to execute on very simple computer
 (without huge amount of virtual memory, CPU, etc.).
 Code should works under both versions of Python (2.X, 3.X).
 In result script runs in Python 3.6 an also Python 2.7.15.
 Python 2.7.15 runs with max_range up to 1000000.
 """

import sys


def square_large_list(list_range):  # creates generator with max_range
    for num in range(0, list_range):
        yield num * num  # returns squared iterator


max_range = 100000000000
if sys.version_info < (3, 0, 0):
    max_range = 1000000  # for Python 2.X max_range limited to 1000000
for number in square_large_list(max_range):
    print(number)
