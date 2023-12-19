
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

class FibonacciGenerator:
    def __init__(self, limit):
        self.first = 1
        self.second = 2
        self.counter = 1

        self.limit = limit

    def __iter__(self):

        return self.counter

    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration

        result = self.first
        self.first, self.second = self.second, self.first + self.second
        self.counter += 1
        return result
print()

generator = FibonacciGenerator(10)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
