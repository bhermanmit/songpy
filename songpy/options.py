"""Options class, contains options for SongPy
"""

import argparse


class Options():

    """Contains options for SongPy
    """

    Parser = argparse.ArgumentParser(description='Read in SongPy options.')
    Parser.add_argument('-a', '--artist', dest='artist',
                        help='Artist of the song.')
    Parser.add_argument('-s', '--song', dest='song',
                        help='Title of song.')

    def __init__(self):

        self._artist = None
        self._song = None

        args = Options.Parser.parse_args()
        self.artist = args.artist
        self.song = args.song

    def __str__(self):

        string = ""
        string += "Options class\n"
        string += "------------\n"

        string += 'Artist: {}\n'.format(self.artist)
        string += 'Song: {}\n'.format(self.song)

        return string

    @property
    def artist(self):

        """The artist of the song.

        Returns
        -------
        str
        """

        return self._artist

    @artist.setter
    def artist(self, artist):

        """The artist of the song.

        Parameters
        ----------
        artist : str
        """

        if not isinstance(artist, str):
            raise TypeError("Artist is not a string.")

        self._artist = artist

    @property
    def song(self):

        """The title of the song.

        Returns
        -------
        str
        """

        return self._song

    @song.setter
    def song(self, song):

        """The title of the song.

        Parameters
        ----------
        song : str
        """

        if not isinstance(song, str):
            raise TypeError("Song is not a string.")

        self._song = song