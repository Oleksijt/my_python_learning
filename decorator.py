
def square_large_list(list_range):  # creates generator with max_range
    i = 0
    while i < list_range:
        yield i * i  # returns squared iterator
        i += 1


max_range = 100000000000
for number in square_large_list(max_range):
    print(number)
