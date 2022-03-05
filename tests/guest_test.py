# guest_test.py - Testing my guest.py file.

import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Colonel Mustard", 16, 20, "Space Oddity", 5)
        self.guest_2 = Guest("Mrs Peacock", 21, 10, "Stairway to Heaven", 3)
        self.guest_3 = Guest("Professor Plum", 54, 9, "Love Spreads Around", 8)

    def test_guests_have_name(self):
        self.assertEqual("Colonel Mustard", self.guest_1.guest_name)
        self.assertEqual("Mrs Peacock", self.guest_2.guest_name)
        self.assertEqual("Professor Plum", self.guest_3.guest_name)

    def test_guests_have_wallet(self):
        self.assertEqual(20, self.guest_1.guest_wallet)
        self.assertEqual(10, self.guest_2.guest_wallet)
        self.assertEqual(9, self.guest_3.guest_wallet)