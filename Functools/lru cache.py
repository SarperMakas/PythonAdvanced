"""lru cache"""
from functools import lru_cache
import time

# maxsize = how many last recent calls do you want to recall

@lru_cache(maxsize=2)
def fib(n):
    if n < 2:
        return n
    print(f"calculating fib {n}")
    return fib(n-1) + fib(n-2)

s = time.time()
[fib(x) for x in range(30)]

# with out lru_cache it is ~9 seconds.
# now it is 0.07s
print(time.time()-s)

print(fib.cache_info())