# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item 

class Room():

    def __init__(self, room_name, description, item):
        self.room_name = room_name
        self.description = description
        self.item = item
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        
    def __str__(self):
        return f"{self.room_name}, {self.description}, {self.item}"



