"""Get the album art.
"""
import urllib2
import urllib
import json


class AlbumArt(object):

    def __init__(self, details):
        self.artist = details.artist.decode('utf-8')
        self.song = details.song.decode('utf-8')
        self.search_query = ''
        self.artist_tag = ''
        self.song_tag = ''
        self.album_tag = ''
        self.artwork_url = ''
        self.genre_tag = ''
        self.release_date_tag = ''
        self.track_tag = ''
        self.image_path = ''

        self.create_query()
        self.download_image()

    def create_query(self):
        itunes_search = 'https://itunes.apple.com/search?term='
        query = self.artist.replace(' ', '+') + '+' + self.song.replace(' ', '+')
        query = query.replace('&', '%26')
        self.search_query = itunes_search + query

    def download_image(self):
        response = urllib2.urlopen(self.search_query)
        data = json.load(response)
        self.artist_tag = data["results"][0]["artistName"].decode('utf-8')
        self.song_tag = data["results"][0]["trackName"].decode('utf-8')
        self.album_tag = data["results"][0]["collectionName"]
        self.genre_tag = data["results"][0]["primaryGenreName"]
        self.release_date_tag = data["results"][0]["releaseDate"]
        self.artwork_url = data["results"][0]["artworkUrl100"]
        self.track_tag = data["results"][0]["trackNumber"]
        self.artwork_url = self.artwork_url.replace("/100x100bb", "/1000x1000bb")
        self.image_path = "/Users/crherman7/Pictures/" + self.artist_tag + ' - ' \
                          + self.song_tag + '.jpg'
        image = urllib.URLopener()
        image.retrieve(self.artwork_url, self.image_path)