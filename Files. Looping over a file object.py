try:
    f = open('testfile.txt', 'r')
    for data in f:
        print(data)
except File:
    print('File not found')