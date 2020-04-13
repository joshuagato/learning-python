class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the song's creator.
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """ Song init method """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year

        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # we've just read details for a new artist
                # retrieve the artist object if there is one, otherwise,
                # create a new artist object and add it to the artist list.
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # we've just read a new album for the current artist
                # store current album in the artist' collection and then create a new album object
                new_album = find_object(album_field, new_album.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

# help(Song)
# help(Song.__init__)
# print(Song.__doc__)
# print(Song.__init__.__doc__)