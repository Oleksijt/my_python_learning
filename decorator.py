import datetime


def run_time(func):

    def wrapper(*args, **kwargs):
        begin = datetime.datetime.now()
        func(*args, **kwargs)
        print('The function {} has been running for {} seconds.'.format(
            func,
            (datetime.datetime.now() - begin).total_seconds()
             ))
    return wrapper


@run_time
def square_large_list(list_range):  # creates generator with max_range
        i = 0
        while i < list_range:
            print(i**2)  # prints squared iterator
            i += 1


square_large_list(100)
