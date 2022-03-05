# song_test.py - Testing my song.py file.

import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song ("Space Oddity")
        self.song_2 = Song ("Comfortably Numb")
        self.song_3 = Song ("When the Music's Over")
    
    def test_songs_have_name(self):
        self.assertEqual("Space Oddity", self.song_1.song_name)
        self.assertEqual("Comfortably Numb", self.song_2.song_name)
        self.assertEqual("When the Music's Over", self.song_3.song_name)