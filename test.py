def a():
    x = 5
    yield x
    x = 6
    yield x
b = a()
print (next(b))
print (next(b))