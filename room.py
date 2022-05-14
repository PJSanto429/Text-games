'''Room class. extremely bare bones and unfinished.'''

import sys
from time import sleep
import gc
from object import Object

def type_effect(text = ""):
    words = text
    for char in words:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()


class Player():
    def __init__(self, room):
        self.room = room

player = Player('kitchen')

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
        
    def action(self, action, player_room):
        #print()
        #type_effect(f'action: {action} - player room: {player_room}')
        for i in Room.instances:
            if i.name == player.room:
                if action == 'look':
                    i.room_description(player_room)
                if action == 'move':
                    pass

    def room_description(self, player_room):
        for i in Room.instances:
            if i.name == player_room:
                print()
                type_effect(i.description)
                print()
                type_effect('You can see ')
                x = 0

        for i in Object.instances:
            if i.room == player_room:
                if x == 0:
                    type_effect(i.longName)
                    x += 1
                else:
                    type_effect(f', {i.longName}')
                    x += 1

        if x == 0:
            print()
            type_effect('nothing...')

        print()
        type_effect('You can go:')
        
        for i in Room.instances:
            if i.name == player_room:
                if i.north != False:
                    print()
                    type_effect('north')
                if i.south != False:
                    print()
                    type_effect('south')
                if i.east != False:
                    print()
                    type_effect('east')
                if i.west != False:
                    print()
                    type_effect('west')

    def move_room(self, player_room, direction):
        for i in Room.instances:
            if i.name == player_room:
                if direction == 'north':
                    if i.north != False:
                        player_room = i.north
                        print()
                        type_effect('You have moved North')

                if direction == 'south':
                    if i.south != False:
                        player_room = i.south
                        print()
                        type_effect('You have moved South')

                if direction == 'east':
                    if i.east != False:
                        player_room = i.east
                        print()
                        type_effect('You have moved East')

                if direction == 'west':
                    if i.west != False:
                        player_room =i.west
                        print()
                        type_effect('You have moved West')

    def change_room(self, player_room):
        player_room = player_room

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