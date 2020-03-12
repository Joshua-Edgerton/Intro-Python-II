from room import Room
from player import Player
from item import Item
import os, sys
os.system("cls")

# Small change for git PR

sys.path.append("/items")

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
room["foyer"].set_items([Item("Orb of Experience", "Grants double EXP")])
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room["overlook"].set_items([Item("Book of code skills", "Adds +50 Awesomeness")])
room["overlook"].set_items([Item("Mana vial", "Adds +30 Mana")])
room['narrow'].w_to = room['foyer']
room["narrow"].set_items([Item("Health vial", "Adds +25 Health")])
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Type in your characters name: ")
player = Player(player_name, room['outside'], 100, 200, 100, 1)

# Write a loop that:
#a
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
    print(f"\n\u001b[31mDeaths: {deaths} \n\u001b[34mEXP: {exp}/100 \n\u001b[32mLevel: {level}\u001b[37m")
    print(player)
    #read
    cmd = input("Directional Controls: \u001b[34m[n] [s] [e] [w]\u001b[37m \nOpen Item Menu: \u001b[34m[i]\u001b[37m\nCharacter Stats: \u001b[34m[c]\u001b[37m\n\u001b[33mInput : \u001b[37m")
    #Item effects
    if "Orb of Experience" in str(player.stash):
        player.multiplier = 2
    if "Book of code skills" in str(player.stash):
        player.awesomeness = player.awesomeness + 50
    if "Mana vial" in str(player.stash):
        player.mana = player.mana + 30
    if "Health vial" in str(player.stash):
        player.health = player.health + 25
    #Evaluate
    try:
        if cmd == "q":
            print("Goodbye!")
            break

        if cmd == 'n' or cmd == 'e' or cmd == 's' or cmd == 'w':
            attrib = f'{cmd}_to'
            print(str(player.stash) + "player stash here")

            if player.current_room.__dict__[attrib] == None:
                print(
                    "\n\u001b[31m !!!! You've chosen a fatal direction and have respawned at the entrance !!!!\n You will still keep your items")
                deaths = deaths + 1
                player = Player(player_name, room['outside'], 100, 100, 100, player.multiplier) 
# * Prints the current room name
            else:
                player.current_room = player.current_room.__dict__[
                    attrib]
                print(player)
                if "Orb of Experience" in str(player.stash):
                    multiplier = 2
                else:
                    multiplier = 1
                
                exp = exp + 10 * multiplier
                if exp > 99:
                    remaining_exp = exp - 100
                    exp = remaining_exp
                    level = level + 1
                    talents = input("You leveled up! Choose a bonus! \n [h] Health\n [m] Mana\n [a] Awesomeness\n\u001b[33mInput :\u001b[37m ")
                    if talents == "h":
                        player.health = player.health + 15
                        print("\nPlayer health has increased to " + str(player.health) + "!!")
                    elif talents == "m":
                        player.mana = player.mana + 20
                        print("\nPlayer mana has increased to " + str(player.mana) + "!!")
                    elif talents == "a":
                        player.awesomeness = player.awesomeness + 50
                        print("\nPlayer awesomeness has increased to " + str(player.awesomeness) + "!!")
        elif cmd == "i":
            if player.stash == []:
                print("\n\u001b[31mNo items in inventory\u001b[37m")
            else:
                print(player.stash)
            roomitems = []
            stashitems = []
            if player.stash:
                for i in player.stash:
                    stashitems.append(i)
            else:
                stashitems = "\u001b[31m[No items in inventory]\u001b[37m"
            if player.current_room.items:
                for i in player.current_room.items:
                    roomitems.append(i.name)
            else:
                roomitems = "\u001b[31m[No items in room]\u001b[37m"
            select = input("Inventory Controls:\n \u001b[34m[b]\u001b[37m Back\n \u001b[34m[p]\u001b[37m Pickup Items in room: \u001b[34m" + str(roomitems) + "\u001b[37m\n \u001b[34m[d]\u001b[37m Drop Items here: \u001b[34m"  + str(stashitems) + "\u001b[37m\n\u001b[33mInput :\u001b[37m ")

            if select == "b":
                pass
            elif select == "p":
                for i in roomitems:
                    confirm = input("Are you sure you wish to pick up " + str(i) + "? \u001b[34m[y] [n]\u001b[37m : ")
                    if confirm == "y":
                        player.stash.append(i)
                        print("You've acquired " + i + "!!")
                        if player.current_room.items[0].name == i:
                            del player.current_room.items[0]
                            print("\nRemoved " + str(i) + " from " + str(player.current_room.name) + "")
                        elif player.current_room.items[1].name == i:
                            del player.current_room.items[1]
                            print("\nRemoved " + str(i) + " from " + str(player.current_room.name) + "")
                        elif player.current_room.items[2].name == i:
                            del player.current_room.items[2]
                            print("\nRemoved " + str(i) + " from " + str(player.current_room.name) + "")
                        elif player.current_room.items[3].name == i:
                            del player.current_room.items[3]
                            print("\nRemoved " + str(i) + " from " + str(player.current_room.name) + "")
            elif select == "d":
                for i in player.stash:
                    dropchoice = input("Are you sure you want to drop " + i + " in " + "? \u001b[34m[y] [n]\u001b[37m : ")
                    if dropchoice == "y":
                        player.current_room.set_items([Item(i, "Dropped item")])
                        player.stash.remove(i)
                    elif dropchoice == "n":
                        print("Declined to drop " + i)
                    else:
                        print("Invalid input")
                        pass
            else:
                pass
        elif cmd == "c":
            print("\nHere you can view your character stats\n")
            print("\u001b[31mHealth: \u001b[37m", player.health, "")
            print("\u001b[34mMana:\u001b[37m ", player.mana, "")
            print("\u001b[32mAwesomeness: \u001b[37m", player.awesomeness, "")
            print("\u001b[33mExperience Multiplier:\u001b[37m x", player.multiplier, "")
            back = input("\nPress \u001b[34m[b] \u001b[37mto go back\n\u001b[33mInput\u001b[37m : ")
            if back == "b":
                pass
            else:
                print("Invalid input")
        else:
            print('Invalid input. Please try again.\n')
    except ValueError:
        print('Invalid input.\n')