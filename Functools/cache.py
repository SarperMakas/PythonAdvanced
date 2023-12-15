"""
Sometimes called "memoize".

"""

from functools import cache
import time

@cache
def add(x, y):
    """Adds two numbers together."""

    print("running")
    time.sleep(2)
    return x + y

# cache remembers parameter and return value combination (ordering maters)
# first function is going to run but second one do not run because we already know the return value
print("NOT CACHED", add(2, 5))
print("CACHED", add(2, 5), "\n")

# these two functions going to run
print("NOT CACHED", add(6, 5))
print("NOT CACHED", add(3, 5))

