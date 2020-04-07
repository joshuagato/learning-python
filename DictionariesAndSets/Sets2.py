print("=" * 150)

even = set(range(0, 40, 2))
print(sorted(even))

square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)
print(sorted(squares))

print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

print("=" * 150)

even = set(range(0, 40, 2))
print(sorted(even))

square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)
print(sorted(squares))

print()

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print()

print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

print("=" * 150)

squares.discard(4)
squares.remove(16)
squares.discard(8)  # no error, does nothing
print(squares)

# squares.remove(8) # breaks the app and shows error
# print(squares)

try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set.")

print(squares)

print("=" * 150)    # ==========================================

even = set(range(0, 40, 2))
print(even)

square_tuple = (4, 6, 16, 26)
squares = set(square_tuple)
print(sorted(squares))

if squares.issubset(even):
    print("Squares is a subset of Even")

if even.issuperset(squares):
    print("Even is a superset of Squares")

print("=" * 150)    # ==========================================

even = frozenset(range(0, 100, 2))
print(even)

print("=" * 150)    # ==========================================
