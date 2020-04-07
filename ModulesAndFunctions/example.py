import shelve

print()
print(dir())
print()

print(dir(__builtins__))
print()

print(dir(__annotations__))
print()

for m in dir(__builtins__):
    print(m)
print()

print(dir(shelve))
print()
