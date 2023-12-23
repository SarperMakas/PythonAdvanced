from typing import TypeAlias

# marked with TypeAlias to make it explicit that this  is  a type alias, not a normal variable assignment
Vector: TypeAlias = list[float]
print(type(Vector))