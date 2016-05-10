"""Contains main execution routine when calling entry point.
"""

import sys

from src import options, album_art, set_tags
from src import search_youtube


def main():

    details = options.Options()
    youtube_results = search_youtube.SearchYoutube(details)
    album_data = album_art.AlbumArt(details)
    id_tags = set_tags.SetTags(youtube_results, album_data)

if __name__ == '__main__':
    sys.exit(main())
