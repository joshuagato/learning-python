# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

print()

parrot_list = ["non panin'", "no more", "a stiff", "bereft of live"]

parrot_list.append("A Nowegian Blue")

for state in parrot_list:
    print("This parrot is: " + state)

print()

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

print()

# However, this line of code works perfectly =>
numbers_in_order = sorted(numbers)
print(sorted(numbers))

print()

if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are  not equal")

print()

# The sort() method does not return a sorted list therefore, print(numbers.sort()) does not work
# it does not create a new object, however, operates only on the object on which it was called...
numbers.sort()
print(numbers)

print()

if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are  not equal")

print()

if numbers_in_order == sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are  not equal")
