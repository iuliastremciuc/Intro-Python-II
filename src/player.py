# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player(Room):
    def __init__(self, player_name, room_name):
        # super().__init__(room_name, description)
        self.room_name = room_name
        self.player_name = player_name
    def __str__(self):
        return "{}, {}".format(self.player_name, self.room_name)


# player = Player("Bob", 'foyer')
# print(player)