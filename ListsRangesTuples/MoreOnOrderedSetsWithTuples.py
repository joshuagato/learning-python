imelda = "More Mayhem", "Emilda May", 2011, ((1, "Pulling the Rug"), (2, "Pyscho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

imelda2 = "More Mayhem", "Emilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Pyscho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

imelda3 = "More Mayhem", "Emilda May", 2011, (1, "Pulling the Rug"), (2, "Pyscho"), \
          (3, "Mayhem"), (4, "Kentish Town Waltz")

print()
print('*' * 100)
print()

metallica2 = ["Ride the Lightening", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)

print()
print('*' * 100)
print()

# Unpacking the tuple
title, artist, year, tracks = imelda2
print("title:{},  artist:{},  year:{},  tracks:{}".format(title, artist, year, tracks))

print()
print('*' * 100)
print()

# Unpacking the tuple
title, artist, year, track1, track2, track3, track4 = imelda3
print("title:{},  artist:{},  year:{},  tracks:{} {} {} {}".format(title, artist, year, track1, track2, track3, track4))

print()
print('*' * 100)
print()

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    print("\t", song)

print()
print('*' * 100)
print()

for song in tracks:
    track, title = song
    print("\t Track number {}, Title: {}".format(track, title))

print()
print('*' * 100)
print()
