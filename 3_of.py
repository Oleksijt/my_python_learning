from datetime import datetime
start_time = datetime.now()

big_list = range(100000000000)

def gen_square(list_of_number):
    for n in list_of_number:
        yield n*n

gen_square_big_list = gen_square(big_list)
for i in gen_square_big_list:
    print(i)

# for i in range(1000000):
#     print(i*i)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
