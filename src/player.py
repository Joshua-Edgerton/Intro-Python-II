# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.stash = []

    def __str__(self):
        return f'\u001b[33m\n{self.name} is located in the {self.current_room}'