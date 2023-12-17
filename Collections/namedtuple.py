"""Namedtuple: tuple + dict"""
from collections import namedtuple

#                   name,   values
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)

print(color)

# using name
print(color.red)
print(color.green)
print(color.blue)

# using index
print(color[0])
print(color[1])
print(color[2])
