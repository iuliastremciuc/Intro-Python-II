# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player():
    def __init__(self, player_name, current_room):
        # super().__init__(room_name, description)
        self.current_room = current_room
        self.player_name = player_name
        self.inventory = []
    def __str__(self):
        return f"{self.player_name}, {self.current_room}, {self.inventory}"

    


player1 = Player("Bob", 'foyer')
print(player1)