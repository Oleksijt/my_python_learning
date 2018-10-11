from datetime import datetime
start_time = datetime.now()

big_list = range(1000)
big_list_square = (n**2 for n in big_list)

print(big_list_square)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
