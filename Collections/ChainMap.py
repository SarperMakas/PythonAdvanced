"""Chain Map | Chaining Multiple Dictionary"""
from collections import ChainMap

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 4, "d": 5, "b": 6}

d = ChainMap(dict1, dict2)
print(d)

print(d['a'])
print(d['d'])
print(d['c'])  # depend on order dict1 have higher order against to dict2
