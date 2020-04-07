print("=" * 150)

farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

print("=" * 150)

for animal in farm_animals:
    print(animal)

print("=" * 150)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])    # the set constructor
print(wild_animals)

print("=" * 150)

for animal in wild_animals:
    print(animal)

print("=" * 150)

farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)

print("=" * 150)    # lines across

empty_set = set()   # creates an empty set with the set constructor
empty_set2 = {}     # creates an empty dictionary

empty_set.add("a")
# empty_set2.add("a")   # this will always result in an error since dictionaries dont have the add method

even = set(range(0, 40, 2))

print("Even: ", end='')
print(even)

print("Length: ", end='')
print(len(even))

print("=" * 150)

square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)

print('Squares: ', end='')
print(squares)

print("=" * 150)

print("Even union Squares: ", end=' ')
print(even.union(squares))

print("Length: ", end='')
print(len(even.union(squares)))

print("=" * 150)

print("Even intersection Squares: ", end=' ')
print(even.intersection(squares))

print("Length: ", end='')
print(len(even.intersection(squares)))
print(even & squares)
print(squares & even)

print("=" * 150)

even = set(range(0, 40, 2))
print(sorted(even))

square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)
print(sorted(squares))

print()

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print()

print("squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))

print("=" * 150)
