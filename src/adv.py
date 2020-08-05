from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Item("Map", "Take a look at the map")),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("Sword", "Sword will help to fight the monster")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("Pill", "Get an extra life")),


    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("Water", "You can drink water")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item("Gold coin", "This is all that left from treasure!")),
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

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
while True:

    print(player.current_room)
    command = input(">>> ").split(',')
    # print(command)
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
            # if there is set that north room as the player's current_room
            player.current_room = player_location.s_to
        else:
            print("You can't go this direction!")
    elif command[0] == 'e':
        if player_location.e_to:
            # if there is set that north room as the player's current_room
            player.current_room = player_location.e_to
        else:
            print("You can't go this direction!")
    elif command[0] == 'w':
        if player_location.w_to:
            # if there is set that north room as the player's current_room
            player.current_room = player_location.w_to
        else:
            print("You can't go this direction!")
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