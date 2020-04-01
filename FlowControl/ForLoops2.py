number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber += char

newNumber = int(cleanedNumber)
print("The  number is {}".format(newNumber))

print()
print()

for state in ["not panin'", "no more", "a stiff", "bereft of lift"]:
    print("This parrot is " + state)

print()
print()

# Here, the third parameter is the steps it should jump
for i in range(0, 100, 5):
    print("i is {} ".format(i))

print()
print()

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("==================================================")
