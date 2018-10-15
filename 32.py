def square_large_list(list_range):  # creates generator with max_range
    for num in xrange (list_range):
        yield num * num  # returns squared iterator


max_range = 10000000000
for number in square_large_list(max_range):
    print(number)
