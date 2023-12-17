"""defaultdict | no worry about if a key isn't exist in a dict"""
from collections import defaultdict

name = "Sarper İsmet Makas"

"""
d = {}
for c in name:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
"""

d = defaultdict(int)
for c in name:
    d[c] += 1

print(d)
print(d['z'])  # default value 0
print()

d = defaultdict(lambda: 2)
for c in name:
    d[c] += 1

print(d)  # values +2
print(d['z'])  # default value 2
