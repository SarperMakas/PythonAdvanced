"""UserList | for creating custom lists"""
from collections import UserList

class MyList(UserList):
    def pop(self, s=None):
        return False


L = MyList([1, 4, 3, 2])
print(L)
print(L.pop(1))
print(L)
