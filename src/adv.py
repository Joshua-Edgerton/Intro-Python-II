from room import Room
from player import Player
import os

# Small change for git PR
# REPL

deaths = 0
level = 0
exp = 0

choices = ['n', 's', 'e', 'w']

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Newb', room['outside'])

for r in room:
    print(r)

print(player.current_room.name)

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

while True:
    #print
    print(f"\n Deaths: {deaths} \n EXP: {exp}/100 \n Level: {level} \n Current Location:", player.current_room.name, "\n \n ")
    #read
    cmd = input("Choose a Direction to Travel: ")
    #evaluate
    try:
        if cmd == "q":
            print("Goodbye!")
            break
        if cmd == 'n' or cmd == 'e' or cmd == 's' or cmd == 'w':
            attrib = f'{cmd}_to'

            if player.current_room.__dict__[attrib] == None:
                print(
                    "\nYou've chosen a fatal direction and must start over")
                deaths = deaths + 1
                player = Player('Newb', room['outside']) 
# * Prints the current room name
            else:
                player.current_room = player.current_room.__dict__[
                    attrib]
                print(player)

        else:
            print('Invalid input. Please try again.\n')
    except ValueError:
        print('Invalid input.\n')




            # player = Player('Newb', room['outside'].n_to)
            # print("You went north to", player.room.name)