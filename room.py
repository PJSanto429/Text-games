'''Room class. extremely bare bones and unfinished.'''

import sys
from time import sleep
import gc

def type_effect(text = ""):
    words = text
    for char in words:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

class Room():
    instances = []
    def __init__(self, name = 'void', description = 'void', north = False, south = False, east = False, west = False):
        self.__class__.instances.append(self)
        self.name = name
        self.description = description

        self.north = north
        self.south = south
        self.east = east
        self.west = west
        
    def action(self, action = 'none', name = 'none'):
        roomList = []

        for i in Room.instances:
            print()         #add same thign as Object.action FJKLSDFJKSDFJKFJWQERWIOQRHEWUN;SDJAFWEUIFBSDJKALFBSDJKLA
            type_effect(i.name)

    def room_description(self):
        return(self.description)

    def set_directions(self, north = False, south = False, east = False, west = False):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def change_description(self, description = 'void'):
        self.description = description

    def test(self, action = 'all'):
        if action == 'all':
            print()
            type_effect(f"Name: {self.name}")
            print()
            type_effect(f"Description: {self.description}")
            print()
            type_effect(f'north: {self.north}')
            print()
            type_effect(f'south: {self.south}')
            print()
            type_effect(f'east: {self.east}')
            print()
            type_effect(f'west: {self.west}')

        elif action == 'every':
            for i in Room.instances:
                print()
                type_effect(i.name)