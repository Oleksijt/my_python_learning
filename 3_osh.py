import sys

from datetime import datetime
start_time = datetime.now()

big_number = 100000000000
big_list = []

if sys.version[0] == '2':
    big_list = xrange(big_number)
elif sys.version[0] == '3':
    big_list = range(big_number)


big_list_square = (n**2 for n in big_list)
for n in big_list_square:
    print(n)


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))