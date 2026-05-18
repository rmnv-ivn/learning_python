a, b = 1, 2
print(a, b)
print(id(a), id(b))
a, b = b, a
print(a, b)
print(id(a), id(b))
print(type(a))