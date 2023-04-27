a = "Hello"
b = "Hello"

print(id(a), id(b))
print(a is b)
print(a in b)
print(a == b)

b = b[:-1] + "o"
print(b)

print(id(a), id(b))
print(a is b)
print(a in b)
print(a == b)
