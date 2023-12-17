"""Counter"""
from collections import Counter

counter1 = Counter(['A', 'A', 'A', 'B', 'B', 'C', 'c'])
counter2 = Counter({'A': 3, 'B': 2, 'C': 1, 'c': 1})
counter3 = Counter(A=3, B=2, C=1, c=3, d=10)

print("Counter1:", counter1)
print("Counter2:", counter2)
print("Counter3:", counter3)
print("==:", counter2 == counter1)
print()
counter3.update(counter1)
print("Update:", counter3)
print()
print("1 Values", counter1.values())
print("1 Keys", counter1.keys())
print("1 Total", counter1.total())
print("2 Elements as list", list(counter2.elements()))
print("3 Most Com 2:",counter3.most_common(2))
