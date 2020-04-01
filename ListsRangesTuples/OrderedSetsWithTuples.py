t = "a", "b", "c"
print(t)

print("a", "b", "c")

print(("a", "b", "c"))

print()
print('*' * 100)
print()

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011

metallica = "Ride the Lightening", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[2])

print()
print('*' * 100)
print()

print(imelda)
imelda = imelda[0], "Imdelda May", imelda[2]
print(imelda)

print()
print('*' * 100)
print()

# Unpacking the tuple
title, artist, year = imelda
print("title:{}, artist:{}, year:{}".format(title, artist, year))

print()
print('*' * 100)
print()
