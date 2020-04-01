age = 24
# print("My name is " + age + " years")   # This would result in an error

print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

print()

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "January", "March",
    "May", "July", "August", "October", "December"))

print()

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {1}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

print()

# %d represents integers and %s represents strings
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

print()

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

print()

# %f represents floating point numbers
print("Pi is approximately %12.50f" % (22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))

print()

# Here, {0:2} 0 represents the replacement field index and 2 represents the width
# Hence, 0 represents the 1st spot while 1 represents the 2nd spot
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
