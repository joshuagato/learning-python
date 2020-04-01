list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

print()

if list_1 == list_2:
    print("The lists are equal")

print()

print(list("The lists are equal"))

print()

# Here, both even and another_even are sorted
even = [2, 4, 6, 8]
another_even = even
# another_even.sort(reverse=True)
# sorted(another_even, reverse=True)
print(even)

print()

# Therefore here, the (is) evaluation results to true
# Also, (==) evaluates to true
print(another_even is even)
print(another_even == even)

print()
print("################################################################################################")
print()

# However, here, a new list is created by invoking the list constructor list()
even2 = [2, 4, 6, 8]
another_even2 = list(even2)
# another_even2.sort(reverse=True)
# sorted(another_even2, reverse=True)
print(even2)

print()

# Therefore here, the (is) evaluation results to false
# However, (==) evaluates to true
print(another_even2 is even2)   # checks for equality of the memory location
print(another_even2 == even2)   # checks for equality of the content

print()
print("################################################################################################")
print()

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

print()

for numbers_set in numbers:
    print(numbers_set)

    for value in numbers_set:
        print(value)

print()
print("################################################################################################")
print()

menu = []
# menu = list()
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

for meal in menu:
    # if not "spam" in meal:  # The linter told me to use (<var> not in) instead of (not <var> in)
    if "spam" not in meal:
        print(meal)

        for ingredient in meal:
            print(ingredient)

string = "1234567890"
for char in string:
    print(char)

print()

my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# Here, if we go beyond the number of items in the iterable, by accessing an element which is not in
# we have ab error

print()
print("################################################################################################")
print()

string = "1234567890"

for char in string:
    print(char, end='')

print()

for char in iter(string):
    print(char, end='')

print()

print()
print("################################################################################################")
print()
