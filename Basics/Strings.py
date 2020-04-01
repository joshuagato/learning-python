parrot = "Norwegian Blue"
print(parrot)

print()

print(parrot[3])
print(parrot[0])

print()

print(parrot[-1])   # Gets the last character

print()

# error
# print(parrot[14])

# range length of 6characters starting at index 0
print(parrot[0:6])

# Would automatically print from the 1st character plus 6 characters
print(parrot[:6])

# Prints from index 6 (7th character to the end)
print(parrot[6:])

# Prints from the end and moves backwards 2 characters
print(parrot[-4:-2])

# Start from index 0 up to but not including index 6, in 2 steps
print(parrot[0:6:2])

# Start from index 0 up to but not including index 6, in 3 steps
print(parrot[0:6:3])

print()

number = "9,223,372,036,854,775,807"
print(number[1::4])

numbers = "1, 2, 3, 4, 5, 6, 7, 7, 8, 9"
print(numbers[0::3])

print()

string1 = "he's "
string2 = "probably "
print(string1 + string2)

print("he's " "probably " "pining")
print("he's probably pining")

print()

print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

print()

today = "friday"
print("day" in today)   # Checks whether day can be found in the string friday

print("fri" in today)   # Checks whether fri can be found in the string friday

print("thur" in today)   # Checks whether thur can be found in the string friday

print("parrot" in "fjordas")   # Checks whether thur can be found in the string friday