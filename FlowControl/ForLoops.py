# Prints from 1 to 19
for i in range(1, 20):
    print("i is now {}".format(i))

print()

number = "9, 223, 372, 036, 854, 775, 807"
for i in range(0, len(number)):
    print(number[i], end='')

print()
print()

number = "9, 223, 372, 036, 854, 775, 807"
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')

print()
print()

number = "9, 223, 372, 036, 854, 775, 807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))
