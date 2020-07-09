from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
outside_room = room['outside']
foyer_room = room['foyer']
narrow_room = room['narrow']
overlook_room = room['overlook']
treasure_room = room['treasure']

# x = input("Enter a command: ")
# y = input("Welcome to the GAME! \nYou are in !" + str(outside_room))
new_player = Player("Nat", room['outside'].room_name)
print(new_player)
while True:
    print("Welcome to the GAME! " )
    y = input("Enter your name: ")
    player1 = Player(str(y), room['outside'].room_name )
    print("Welcome " + player1.player_name + " you are --> " + str(outside_room))
    print("Press 'n' to proceed!!")
    x = input("Enter a command: ")
    while True:
        if x == 'n':
            print("You are in " +str(foyer_room))
        else:
            print("The only way to start game it's to go North. \n Please press 'n'!")###### can't understand why it print this inside of nested loop
        x = input("Enter a command: ")
        # break
        while True:
            if x  == 'e':
                print("You are in " + str(narrow_room))
                x = input("Enter a command: ")
                while True:
                    if x == 'w':
                        print("You are back in " + str(foyer_room))
                    elif x == 'n':
                        print("You are in the " + str(treasure_room))
                        x = input("Enter a command: ")
                        if x == 's':
                            print("You are back in the " + str(narrow_room))
                        else:
                            print("Stuck in this room forever!!!")
                        break
                    else:                    
                        print("Got lost forever....")
                        

                    x = input("Enter a command: ")
                    break
            elif x == 'n':
                print("You are in " + str(overlook_room))
                x = input("Enter a command: ")
                while True:
                    if x == 's':
                        print("You are back in " + str(foyer_room))
                    else:
                        print("You are falling off the cliff!!!!!!")
                    x = input("Enter a command: ")

            elif x == 's':
                print("You are back in " + str(outside_room)) # it's treaky, can't figure out how to direct it to previous loop
            else:
                print("Invalid move! \nFrom foyer you can go only 's', 'n', 'e'!!!")
            break

#####Two last command output are from previous loops
          
# Welcome to the GAME!
# Enter your name: man
# Welcome man you are --> Outside Cave Entrance, North of you, the cave mount beckons
# Press 'n' to proceed!!
# Enter a command: n
# You are in Foyer, Dim light filters in from the south. Dusty
# passages run north and east.
# Enter a command: e
# You are in Narrow Passage, The narrow passage bends here from west
# to north. The smell of gold permeates the air.
# Enter a command: n
# You are in the Treasure Chamber, You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.
# Enter a command: s
# You are back in the Narrow Passage, The narrow passage bends here from west
# to north. The smell of gold permeates the air.
# The only way to start game it's to go North.
#  Please press 'n'!
# Enter a command: n
# You are in Grand Overlook, A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.




# main()

# new_player = 

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
