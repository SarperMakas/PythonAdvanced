"""cached property"""

from functools import cached_property

"""
# property is kind of getter in python

class Marksheet:
    def __init__(self, *grades):
        self.grades = grades

    @property
    def total(self):
        print("Calculating total...")
        return sum(self.grades)

    @property
    def average(self):
        print("Calculating avarage...")
        return self.total/len(self.grades)

m = Marksheet(100, 90, 95)
print(m.average)
"""

class Marksheet:
    def __init__(self, *grades):
        self.grades = grades

    @cached_property
    def total(self):
        print("Calculating total...")
        return sum(self.grades)

    @cached_property
    def average(self):
        print("Calculating avarage...")
        return self.total/len(self.grades)

m = Marksheet(100, 90, 95)

# property runs only once
# cached property is based on class parameters
print(m.average)
print(m.average)
m.grades = (20, 30, 40)
print(m.average)