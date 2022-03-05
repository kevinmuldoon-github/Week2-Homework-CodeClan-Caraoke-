# room_test.py - Testing my room.py file.

import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("The Fancy Room")
        self.room_2 = Room("The Cheap Room")
        self.room_3 = Room("The Loud Room")
        
    
    def room_has_name(self):
        self.assertEqual("The Fancy Room99", self.room_1)