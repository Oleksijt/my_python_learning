from builtins import print

x = 11


def g1():
    print(x)


def g2():
    global x
    x = 22


def h1():
    x = 33

    def nested():
        print(x)
def h2():
    x = 33
    def nested():
        nonlocal x
        x = 44
        print(x)

print(x)
g1()
g2()
print(x)
h1()
print(x)
h2()
print(x)
