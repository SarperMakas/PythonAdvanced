
x: tuple[int] = (5,)
y: tuple[int, str] = (5, "foo")
z: tuple[int, ...] = (1, 2, 3)

print(type(x), type(y), type(z))

a: tuple[()] = ()
print(a)
