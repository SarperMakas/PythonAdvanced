"""
singledispatch
*Generics*
"""

from functools import singledispatch

@singledispatch
def append_one(obj):
    print("Unsupported type")
    return obj

@append_one.register(list)
def _(obj):
    return obj + [1]

@append_one.register(set)
def _(obj):
    return obj.union({1})

@append_one.register(str)
def _(obj):
    return obj + "1"

print(append_one([1, 2, 3]))
print(append_one({1, 2, 3}))
print(append_one("2"), "\n")

# if type is not supported original function is called
print(append_one(2))