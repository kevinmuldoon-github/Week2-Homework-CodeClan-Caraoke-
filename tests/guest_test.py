# guest_test.py - Testing my guest.py file.

import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Colonel Mustard")
        self.guest_2 = Guest("Mrs Peacock")
        self.guest_3 = Guest("Professor Plum")