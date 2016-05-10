"""SongPy class, performs operations with youtube
"""


class SongPy(object):

    """Performs operations with youtube
    """

    def __init__(self, options):
        self._options = options

    def __str__(self):

        string = ""
        string += "SongPy class\n"
        string += "------------\n"

        string += str(self._options)

        return string

    def print_options(self):
        print self._options.song
        print self._options.artist