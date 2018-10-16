"""
Calculate squares of numbers.
"""
import sys

NUMBERS = 100000000000

if sys.version_info[0] == 2:
    gen_exp = (x*x for x in xrange(NUMBERS))
else:
    gen_exp = (x*x for x in range(NUMBERS))


if __name__ == '__main__':
    for num in gen_exp:
        print(num)
