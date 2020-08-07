# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item 


class Player():
    def __init__(self, player_name, current_room):
        # super().__init__(room_name, description)
        self.current_room = current_room
        self.player_name = player_name
        self.inventory = []
        

    def take_item(self, i):
        # if i in self.current_room.item:
        self.inventory.append(i)
        
        # if i in self.current_room.item:
            
        #     self.current_room.item.remove(i)
        

    


    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("You don't have this item.")

    def __str__(self):
        return f"{self.player_name}, {self.current_room}, {self.inventory}"

    


# man = Player('man', 'outside')
# print(man.take_item('water'))
# print(man.inventory)