fruit = {
    "orange": "a sweet, orange citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit"
}

print(fruit)

# ordered_keys = list(fruit.keys())   # Convert the dictionary keys into a list
# ordered_keys.sort()   # Sort the items in the list
# for key in ordered_keys:
#     print(key + " - " + fruit[key])
#     print()

# This block of code performs the same functionality as the previous block
# ordered_keys = sorted(list(fruit.keys()))   # Converts the dictionary keys into a list amd sorts the items in the list
# for key in ordered_keys:
#     print(key + " - " + fruit[key])
#     print()

# The previous two blocks of code refactored
for key in sorted(fruit.keys()):
    print(key + " - " + fruit[key])
    print()
