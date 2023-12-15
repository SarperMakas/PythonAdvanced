"""
Use functools.total_ordering
for automatically define __lt__(), __le__(), __gt__(), __ge__() based on
__eg__() and on of the four method.
"""

from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, grade, score):
        self.grade = grade
        self.score = score

    def __eq__(self, other):
        return self.grade == other.grade and self.score == other.score

    def __lt__(self, other):
        return self.grade < other.grade or (self.grade == other.grade and self.score < other.score)


studentA = Student(10, 1)
studentB = Student(12, 1)

# all compressions are working even if we don't define all four
print(studentA == studentB)
print(studentA != studentB)
print(studentA < studentB)
print(studentA <= studentB)
print(studentA > studentB)
print(studentA >= studentB)
