"""Sets the ID3 tags of the song downloaded.
"""
import eyed3


class SetTags(object):

    def __init__(self, youtube_results, album_art):
        self.artist = album_art.artist_tag
        self.song = album_art.song_tag
        self.album = album_art.album_tag
        self.genre = album_art.genre_tag
        self.release_date = album_art.release_date_tag
        self.image = album_art.image_path
        self.track_number = album_art.track_tag
        self.song_path = youtube_results.dest

        self.tagsong()

    def tagsong(self):
        songfile = eyed3.load(self.song_path)
        songfile.tag.artist = self.artist
        songfile.tag.title = self.song
        songfile.tag.album = self.album
        songfile.tag.album_artist = self.artist
        songfile.tag.track_num = self.track_number

        imagedata = open(self.image, "rb").read()
        songfile.tag.images.set(3, imagedata, "image/jpeg", self.artist+' - '+self.song + ' Album Cover')

        songfile.tag.save()
