def createGenerator(lenght) :
    mylist = range(lenght)
    for i in mylist :
        yield i

mygenerator = createGenerator(100000000000) # создаём генератор
for i in mygenerator:
    print(i)