fruit = {
    "orange": "a sweet, orange citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit"
}

print(fruit)
print(fruit["apple"])

print()

fruit["pear"] = "an odd shapped apple"
print(fruit)

print()

fruit["lime"] = "great with tequila"
print(fruit)

print()

# del fruit["lemon"]
# print(fruit)

print()

# The following line will delete the entire dictionary fruit
# del fruit
# print(fruit)

# print()

# The following line will clear the content of fruit into a empty dictionary
# fruit.clear()
# print(fruit)


# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == 'quit':
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#         print()
#     else:
#         print("We don't have " + dict_key)
#         print()


# This block of code functions exactly as the previous block
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == 'quit':
#         break
#     description = fruit.get(dict_key, "We don't have " + dict_key)
#     print(description)
#     print()

print()

print(fruit.items())   # returns a list of tuples

print()
print()

print(tuple(fruit.items()))   # returns a regular tuple of tuples
