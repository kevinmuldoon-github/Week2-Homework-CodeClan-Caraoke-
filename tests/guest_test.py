# guest_test.py - Testing my guest.py file.

import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Colonel Mustard")
        self.guest_2 = Guest("Mrs Peacock")
        self.guest_3 = Guest("Professor Plum")

    def test_guests_have_name(self):
        self.assertEqual("Colonel Mustard", self.guest_1.guest_name)
        self.assertEqual("Mrs Peacock", self.guest_2.guest_name)
        self.assertEqual("Professor Plum", self.guest_3.guest_name)