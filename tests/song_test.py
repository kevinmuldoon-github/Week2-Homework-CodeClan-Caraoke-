# song_test.py - Testing my song.py file.

import unittest
from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song({"Name" : "Space Oddity", "Year of Release" : 1969, "Band" : "David Bowie"})
        self.song_2 = Song({"Name" : "Comfortably Numb", "Year of Release" : 1979, "Band": "Pink Floyd"})
        self.song_3 = Song({"Name" : "When the Music's Over", "Year of Release" : 1967, "Band": "The Doors"})
    
    def test_songs_have_name(self):
        self.assertEqual("Space Oddity", self.song_1.song_details["Name"])
        self.assertEqual("Comfortably Numb", self.song_2.song_details["Name"])
        self.assertEqual("When the Music's Over", self.song_3.song_details["Name"])
