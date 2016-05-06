"""
Project is used to download youtube video into an m4a file and set ID3 tags.
"""
import sys
import options
from youtube import searchyoutube
from idtags import settags
from idtags import albumart


def main():

    details = options.Options()
    youtube_results = searchyoutube.SearchYoutube(details)
    album_art = albumart.Albumart(details)
    idtags = settags.Settags(youtube_results, album_art)

if __name__ == '__main__':
    sys.exit(main())
