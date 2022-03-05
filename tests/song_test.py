# song_test.py - Testing my song.py file.

import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song ("Space Oddity")
        self.song_2 = Song ("Comfortably Numb")
        self.song_3 = Song ("When the Music's Over")