# room.py - Where I check guests in and out of rooms.

class Room:
    
    def __init__(self, room_name, room_capacity, room_fee, bar_capacity):
        self.room_name = room_name
        self.room_capacity = room_capacity # Maximum number of people allowed in the room
        self.room_guests = [] # The guests within the room
        self.room_songs = []  # The songs that are available within the room
        self.room_fee = room_fee # The cost of hiring the room
        self.bar_capacity = bar_capacity # The maximum number of drinks available in the room bar
        self.beers_drunk = 0

    # Simple method to check a guest into a room
    def check_guest_into_room(self, guest):
        self.room_guests.append(guest.guest_name)
        self.drink_a_beer(guest)
    
    # Seperate method to check a guest which also verifies there is space available
    def check_guest_into_room_verify_capacity(self, guest):
        if len(self.room_guests) != self.room_capacity: # Check if there is space for an additional guest
            self.room_guests.append(guest.guest_name)
            self.drink_a_beer(guest)
        else: # No available space for additional guests
            print(f"Sorry, {self.room_name} only has capacity for {self.room_capacity} people.")
            print(f"Currently singing along in {self.room_name}: {self.room_guests}.")
    
    # Separate method to confirm guest has funds to pay the room fee
    def check_guest_has_sufficient_funds(self, guest):
        if self.room_fee > guest.guest_wallet:
            print (f"Sorry, {guest.guest_name} cannot afford CodeClan Caraoke :(")
            return False
        else:
            print (f"{guest.guest_name} has enough money to sing along!")
            return True
    
    # A method to check a guest into a room if they have funds and there is room available for them.
    def check_guest_into_room_verify_funds_and_capacity(self, guest):
        if len(self.room_guests) != self.room_capacity: # Check if there is space for an additional guest
            if self.room_fee > guest.guest_wallet:
                print (f"Sorry {guest.guest_name}. We have room for you, but you do not have enough money to pay for {self.room_name}.")
            else:
                print (f"Yay!!! We have room for {guest.guest_name} and they have enough money to pay {self.room_name} room fee. Enjoy CodeClan Caraoke :)")
                self.room_guests.append(guest.guest_name)
                self.drink_a_beer(guest)
        else: # No available space for additional guests
            print(f"Sorry, {self.room_name} only has capacity for {self.room_capacity} people.")
            print(f"Currently singing along in {self.room_name}: {self.room_guests}.")

    # Method to check a guest out of a room
    def check_guest_out_of_room(self, guest):
        self.room_guests.remove(guest.guest_name)
    
    # Method to add a song to a room
    def add_song_to_room(self, song):
        self.room_songs.append(song.song_details["Name"])

    # Method to remove a song from a room
    def remove_song_from_room(self, song):
        self.room_songs.remove(song.song_details["Name"])
    
    # Method to check if favourite song is playing
    def check_favourite_song_in_room_playlist(self, guest):
        if guest.guest_favourite_song in self.room_songs:
            print(f"Woohoo! {guest.guest_name}'s favourite song {guest.guest_favourite_song} is playing in {self.room_name}.")
    
    # Method to update beers drunk
    def drink_a_beer(self,guest):
        if self.beers_drunk < self.bar_capacity:
            self.beers_drunk += guest.guest_number_of_drinks

    # Method to check bar capacity
    def check_room_bar_drinks_capacity(self):
        self.beers_left = self.bar_capacity - self.beers_drunk
        if self.beers_drunk >= self.bar_capacity:
            print (f"No beers are left in {self.room_name} as {self.beers_drunk} beers have been drunk!")
        else:
            print (f"{self.room_name} has a capacity of {self.bar_capacity} beers and {self.beers_drunk} have been sold already. Only {self.beers_left} are left.")