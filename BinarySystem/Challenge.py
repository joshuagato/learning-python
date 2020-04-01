powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)

print(powers)

# print()
#
# powers = []
# for power in range(15, -2, -1):
#     powers.append(2 ** power)
#
# print(powers)
#
# print()
#
# x = int(input("Please enter a number: "))
#
# for power in powers:
#     print(x // power, end='')
#     x %= power

print()

x = int(input("Please enter a number: "))

printing = False

for power in powers:
    bit = x // power

    if bit != 0 or power == 1:
        printing = True

    if printing:
        print(bit, end='')

    x %= power
exit()