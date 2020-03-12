# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, current_room, health, mana, awesomeness, multiplier):
        self.name = name
        self.current_room = current_room
        self.stash = []
        self.health = 100
        self.mana = 200
        self.awesomeness = 100
        self.multiplier = 1

    def __str__(self):
        return f'\u001b[35m\n{self.name} \u001b[33mis located in the {self.current_room}'