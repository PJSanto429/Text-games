'''Room class. extremely bare bones and unfinished.'''

import sys
from time import sleep

def type_effect(text = ""): #typewriter effect
    words = text
    for char in words:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

class Room():
    def __init__(self, name = 'void', description = 'void', directions = 'none'):
        self.name = name
        self.description = description
        self.directions = directions
        
        self.set_directions()

    def room_description(self):
        pass

    def set_directions(self, test = False):
        if test == False:
            self.directions = self.directions.split()
            if 'north' in self.directions:
                self.north = True
            else:
                self.north = False

            if 'south' in self.directions:
                self.south = True
            else:
                self.south = False

            if 'east' in self.directions:
                self.east = True
            else:
                self.east = False

            if 'west' in self.directions:
                self.west = True
            else:
                self.west = False
        elif test == True:
            if self.north == True:
                type_effect(' north >>')
            if self.south == True:
                type_effect(' south >>')
            if self.east == True:
                type_effect(' east >>')
            if self.west == True:
                type_effect(' west >>')

    def change_description(self, description = 'void'):
        self.description = description

    def test(self, action = 'all'):
        if action == 'all':
            print()
            type_effect(f"Name: {self.name}")
            print()
            type_effect(f"Description: {self.description}")
            print()
            type_effect('Directions: ')
            self.set_directions(True)