print("*" * 150)    # ==============================================================

cities = ["Adelaide", "Alice Spring", "Darwin", "Melbourne", "Sidney"]

# The print statement in this block, does not print to the console, but rather
# prints to the file named "cities.txt"
with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file, flush=True)

cities = []

print("Before: ", end='')
print(cities)

with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print("After: ", end='')
print(cities)
for city in cities:
    print(city)

print("*" * 150)    # ==============================================================

imelda = "More Mayhen", "Imelda May", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhen"), (4, "Kentish Town Waltz")
)

with open("imelda.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)
    print("Done writing to file.")

print("*" * 150)    # ==============================================================

with open("imelda.txt", 'r') as imelda_file:
    contents = imelda_file.readline()
imelda = eval(contents)
print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)

print("*" * 150)    # ==============================================================
