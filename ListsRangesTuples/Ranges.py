print(range(100))

my_list = list(range(10))
print(my_list)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

print()

my_string = 'abcdefghijklmnopqrstuvwxyz'
print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0, 10)
print(small_decimals)
print(small_decimals.index(3))

odd = range(1, 10000, 2)
print(odd)

print(odd[985])

# print()
# print()

# sevens = range(7, 1000000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by seven".format(x))

print()
print()

my_range = small_decimals[::2]  # copy the the entire list in steps of 2
print(my_range)
print(my_range.index(4))

decimals = range(0, 100)
print(decimals)

print()
print("#" * 100)
print()

my_range = decimals[3:40:3]
print(my_range)

print()
print()
print('*' * 100)

for i in my_range:
    print(i, end=' ')

print()
print()
print('*' * 100)

for i in range(3, 40, 3):
    print(i, end=' ')

print()
print()
print('*' * 100)

print(my_range == range(3, 40, 3))

print()
print('*' * 100)
print()

print(range(0, 5, 2) == range(0, 6, 2))
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

print()
print('*' * 100)
print()

r = range(0, 100)
print(r)

# The slice method
for i in r[::-2]:
    print(i, end=' ')

print()
print()

# This is the same as the previous method
for i in range(99, 0, -2):
    print(i, end=' ')

print()

print(range(0, 100)[::-2] == range(99, 0, -2))

print()
print('*' * 100)
print()

# This will not print anything, unless the boundary is reversed as in (100, 0, -2)
for i in range(0, 100, -2):
    print(i)

print()
print('*' * 100)
print()

backString = "egaugnal lufrewop yrev a si nohtyP"
print(backString[::-1])

print()
print('*' * 100)
print()

r = range(0, 10)
for i in r[::-1]:
    print(i, end=' ')
