
def first(n):
    num = 0
    while num < n:
        yield num
        num += 1

generator = first(10000)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))