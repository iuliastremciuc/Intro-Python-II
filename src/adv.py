from room import Room
from player import Player
from item import Item
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Map", "Take a look at the map"), Item("Water", "You can drink water")]),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Sword", "Sword will help to fight the monster"), Item("Water", "You can drink water")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Pill", "Get an extra life"), Item("Water", "You can drink water")]),


    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Water", "You can drink water"), Item("Pill", "Get an extra life")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Gold coin", "This is all that left from treasure!"), Item("Water", "You can drink water")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



# Main

player = Player("name", room['outside'])



print("""HELLO, PLAYER!\nWelcome to the game!\nYou can move by pressing 'n'- north, 's' - south, 'e' - east, 'w' - west or 'q' to quit the game!!!""", '\n')

# Make a new player object that is currently in the 'outside' room.

# Write a loop that: 
while True:
    print("Your location : ", player.current_room)
    print("If you look around, you can see: ", '\n')
    player.current_room.search()
    
   
    # action = input("Choose item: ").lower().split(',')
    # take = player.take_item()
    # drop - player.drop_item()
    print('\n')
    # print("Item in your hand: ", player.inventory, '\n')
    print("Choose your next move!")
    command = input(">>>>>> ").split(' ')
    
    player_location = player.current_room
    
    if command[0] == 'q':
        break    

    elif command[0] == 'n':
        # check if the player can move north
        if player_location.n_to:
            # if there is set that north room as the player's current_room

            player.current_room = player_location.n_to

        else:
            print("You can't go this direction!")
        
    elif command[0] == 's':
        if player_location.s_to:
            # if there is set that south room as the player's current_room
            player.current_room = player_location.s_to
        else:
            print("You can't go this direction!")
    elif command[0] == 'e':
        if player_location.e_to:
            # if there is set that east room as the player's current_room
            player.current_room = player_location.e_to
        else:
            print("You can't go this direction!")
    elif command[0] == 'w':
        if player_location.w_to:
            # if there is set that west room as the player's current_room
            player.current_room = player_location.w_to
        else:
            print("You can't go this direction!")

    elif command[0] == 'take':
        player.take_item(command[1])
    # print(command[0])
        print(player.inventory)
        # else: 
        #     print("Wrong command!")

    elif command[0] == 'drop':
        player.drop_item(command[1])
        print(player.inventory)


#
# * Prints the current room name
# print(playew.current_room)
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.