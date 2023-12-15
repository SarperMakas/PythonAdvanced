"""Partial function"""
from functools import partial

def add(a, b):
    print(f"{a} + {b} = {a + b}")


# run add function with parameters
add(2, 5)

# create predefined add function by using partial function
add2and5 = partial(add, 2, 5)
add4and5 = partial(add, 4, 5)

# run functions with predefined parameters
add2and5()
add4and5()


# can't change parameters after defining
x, y = 3, 5

addXandY = partial(add, x, y)
x, y = 2, 4

addXandY()

# predefined 1 parameter in a functoin that has 2 parameter

add2 = partial(add, 2)  # a is predefined as 2 now
add2(5)

