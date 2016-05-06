"""This class is responsible for searching youtube for song and artist
"""
from __future__ import unicode_literals
from lxml import html
import requests
import youtube_dl
import os
import sys
import difflib


class SearchYoutube(object):
    """Searches youtube for song and artist
    """

    def __init__(self, options):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.artist = options.artist
        self.song = options.song
        self.query = ''
        self.youtube_address = ''
        self.video_address = ''
        self.audio_options = ''
        self.full_song_title = ''
        self.dest = ''

        self.__create_query()
        self.__search()
        self.__set_audio_optins()
        self.__download_video()

    def __create_query(self):
        self.youtube_address = 'https://www.youtube.com'
        pre_query = '/results?search_query='
        resong = self.song.replace(' ', '+')
        resong = resong.replace('&', '%26')
        reartist = self.artist.replace(' ', '+')
        reartist = self.artist.replace('&', '%26')
        self.artist = self.artist.decode('utf-8')
        self.song = self.song.decode('utf-8')
        post_query = reartist + '+' + resong + '+audio'
        self.query = self.youtube_address + pre_query + post_query

    def __search(self):
        page = requests.get(self.query)
        tree = html.fromstring(page.content)
        videos = tree.xpath('//div/h3/a/@href')
        title = tree.xpath('//div/h3/a/@title')
        song_title = title[0]
        self.video_address = self.youtube_address + videos[0]
        id_video_split = self.video_address.split('=')
        id_video = id_video_split[1]
        self.full_song_title = song_title + '-' + id_video + '.mp3'
        print self.full_song_title
        print self.video_address

    def __set_audio_optins(self):
        self.audo_options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]}

    def __download_video(self):
        with youtube_dl.YoutubeDL(self.audo_options) as ydl:
            ydl.download([self.video_address])
        file_path = os.getcwd()
        real_file = ''
        for file in os.listdir(file_path):
            if file.endswith('.mp3'):
                ratio = difflib.SequenceMatcher(None, file, self.full_song_title).ratio()
                if ratio > 0.90:
                    real_file = file
        path = file_path + '/' + real_file
        self.dest = '/Users/crherman7/Music/' + self.artist + ' - ' + self.song + '.mp3'
        os.rename(path, self.dest)
