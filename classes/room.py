# room.py - Where I check guests in and out of rooms.

class Room:
    
    def __init__(self, room_name):
        self.room_name = room_name
        self.room_guests = [] # The guests within the room
        self.room_songs = []  # The songs that are available within the room

    # Method to check a guest into a room
    def check_guest_into_room(self, guest):
        self.room_guests.append(guest.guest_name)

    # Method to check a guest out of a room
    def check_guest_out_of_room(self, guest):
        self.room_guests.remove(guest.guest_name)
    
    # Method to add a song to a room
    def add_song_to_room(self, song):
        self.room_songs.append(song.song_name)

      # Method to remove a song from a room
    def remove_song_from_room(self, song):
        self.room_songs.remove(song.song_name)