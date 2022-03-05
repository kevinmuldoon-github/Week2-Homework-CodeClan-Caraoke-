# room_test.py - Testing my room.py file.

import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        # Define Rooms
        self.room_1 = Room("The Fancy Room")
        self.room_2 = Room("The Cheap Room")
        self.room_3 = Room("The Loud Room")
        # Define Quests
        self.guest_1 = Guest("Colonel Mustard")
        self.guest_2 = Guest("Mrs Peacock")
        self.guest_3 = Guest("Professor Plum")
        # Define Songs
        self.song_1 = Song ("Space Oddity")
        self.song_2 = Song ("Comfortably Numb")
        self.song_3 = Song ("When the Music's Over")

    def test_rooms_have_name(self):
        self.assertEqual("The Fancy Room", self.room_1.room_name)
        self.assertEqual("The Cheap Room", self.room_2.room_name)
        self.assertEqual("The Loud Room", self.room_3.room_name)

    def test_check_guest_into_room(self):
        self.room_1.check_guest_into_room(self.guest_1) # Add Colonel Mustard to Room 1
        self.room_1.check_guest_into_room(self.guest_2) # Add Mrs Peacock to Room 1 too
        self.room_2.check_guest_into_room(self.guest_3) # Add Professor Plum to Room 2
        self.assertEqual("Colonel Mustard", self.room_1.room_guests[0])
        self.assertEqual("Mrs Peacock", self.room_1.room_guests[1])
        self.assertEqual("Professor Plum", self.room_2.room_guests[0])

    def test_check_guest_out_of_room(self):
        # Test 1
        self.room_1.check_guest_into_room(self.guest_1) # Add Colonel Mustard to Room 1
        self.room_1.check_guest_into_room(self.guest_2) # Add Mrs Peacock to Room 1 too
        self.assertEqual("Colonel Mustard", self.room_1.room_guests[0])
        self.assertEqual("Mrs Peacock", self.room_1.room_guests[1])
        self.room_1.check_guest_out_of_room(self.guest_2) # Remove Mrs Peacock from Room 1
        # self.assertEqual("Mrs Peacock", self.room_1.room_guests[1]) # Correctly produces "IndexError: list index out of range"
        # Test 2
        self.room_2.check_guest_into_room(self.guest_3) # Add Professor Plum to Room 2
        self.assertEqual("Professor Plum", self.room_2.room_guests[0])
        self.room_2.check_guest_out_of_room(self.guest_3) # Remove Professor Plum from Room 2
        # self.assertEqual("Professor Plum", self.room_2.room_guests[0]) # Correctly produces "IndexError: list index out of range"
    
    def test_add_song_to_room(self):
        self.room_1.add_song_to_room(self.song_1) # Add Space Oddity to Room 1
        self.assertEqual("Space Oddity", self.room_1.room_songs[0])
    
    def test_remove_song_from_room(self):
        self.room_1.add_song_to_room(self.song_1) # Add Space Oddity to Room 1
        self.assertEqual("Space Oddity", self.room_1.room_songs[0])
        # self.room_1.remove_song_from_room(self.song_1) # Add Space Oddity to Room 1
        # self.assertEqual("Space Oddity", self.room_1.room_songs[0]) # Correctly produces "IndexError: list index out of range"



