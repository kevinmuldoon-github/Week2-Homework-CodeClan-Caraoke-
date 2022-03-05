# room_test.py - Testing my room.py file.

import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        # Define room name, capacity, room fee and maximum amount of drinks available
        self.room_1 = Room("The Fancy Room", 1, 30, 10)
        self.room_2 = Room("The Cheap Room", 2, 10, 7)
        self.room_3 = Room("The Loud Room", 0, 15, 11)

        # Define guest name, guest age, money in wallet, favourite song and desired number of drinks
        self.guest_1 = Guest("Colonel Mustard", 16, 20, "Space Oddity", 5)
        self.guest_2 = Guest("Mrs Peacock", 21, 10, "Stairway to Heaven", 3)
        self.guest_3 = Guest("Professor Plum", 54, 9, "Love Spreads Around", 8)

        # Define songs using dictionary
        self.song_1 = Song({"Name" : "Space Oddity", "Year of Release" : 1969, "Band" : "David Bowie"})
        self.song_2 = Song({"Name" : "Comfortably Numb", "Year of Release" : 1979, "Band": "Pink Floyd"})
        self.song_3 = Song({"Name" : "When the Music's Over", "Year of Release" : 1967, "Band": "The Doors"})

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

    # Question for Instructors: How can we check for an "list index out of range" error without breaking a test?

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

    def test_check_guest_into_room_verify_capacity(self):
        self.room_1.check_guest_into_room_verify_capacity(self.guest_1) # Add Colonel Mustard to Room 1
        self.room_1.check_guest_into_room_verify_capacity(self.guest_2) # Add Mrs Peacock to Room 1 too
        self.room_1.check_guest_into_room_verify_capacity(self.guest_3) # Add Professor Plum to Room 1 too
        self.room_2.check_guest_into_room_verify_capacity(self.guest_1) # Add Colonel Mustard to Room 1
        self.room_2.check_guest_into_room_verify_capacity(self.guest_2) # Add Mrs Peacock to Room 1 too
        self.room_2.check_guest_into_room_verify_capacity(self.guest_3) # Add Professor Plum to Room 1 too

    def test_check_guest_has_sufficient_funds(self):
        self.room_1.check_guest_has_sufficient_funds(self.guest_1)
        self.room_2.check_guest_has_sufficient_funds(self.guest_2)
        self.room_3.check_guest_has_sufficient_funds(self.guest_3)
    
    def test_check_guest_into_room_verify_funds_and_capacity(self):
        self.room_1.check_guest_into_room_verify_funds_and_capacity(self.guest_1)
        self.room_2.check_guest_into_room_verify_funds_and_capacity(self.guest_2)
        self.room_3.check_guest_into_room_verify_funds_and_capacity(self.guest_3)
    
    def test_check_favourite_song_in_room_playlist(self):
        self.room_1.add_song_to_room(self.song_1) # Add Space Oddity to Room 1
        self.room_1.check_favourite_song_in_room_playlist(self.guest_1)

    def test_check_room_bar_drinks_capacity(self):
        self.room_1.check_guest_into_room(self.guest_1) # Add Colonel Mustard to Room 1
        self.room_1.check_guest_into_room(self.guest_2) # Add Mrs Peacock to Room 1
        self.room_2.check_guest_into_room(self.guest_3) # Add Professor Plum to Room 1
        self.room_1.check_room_bar_drinks_capacity()
        