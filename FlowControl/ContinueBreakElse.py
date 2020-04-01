shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
nasty_food_item = ''

for item in shopping_list:
    if item == 'spam':
        print("I am ignoring " + item)
        continue

    print("Buy " + item)

print()
print()

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
nasty_food_item = ''

for item in shopping_list:
    if item == 'spam':
        nasty_food_item = item
        print("I am ignoring the rest of the items")
        break

    print("Buy " + item)

if nasty_food_item:
    print("Can't I have anything without spam in it".format(nasty_food_item))

print()
print()

# shopping_list = ["milk", "pasta", "eggs", "beef", "bread", "rice"]
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
nasty_food_item = ''

for item in shopping_list:
    if item == 'spam':
        nasty_food_item = item
        print("I am ignoring the rest of the items")
        break
    print("Buy " + item)
else:
    print("I'll have a plate of that, then, please")

if nasty_food_item:
    print("Can't I have anything without {} in it".format(nasty_food_item))
