from object import Object
from typeEffect import type_effect
try:
    from debugger import debug
except:
    pass
from random import choice

class Player(): #this is simply so the player can move rooms and it actually work.
    def __init__(self, room):
        self.room = room
player = Player('first')

class Room():
    instances = []
    nameInstances = []
    def __init__(self, name = 'void', description = 'void', north = False, south = False, east = False, west = False):
        self.__class__.instances.append(self)
        self.__class__.nameInstances.append(name)
        self.name = name
        self.description = description

        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.x = 0
        
    def action(self, action, player_room, direction = 'none'):
        for i in Room.instances:
            if i.name == player.room:
                if action == 'look':
                    i.room_description(player.room)
                if action == 'move':
                    i.move_room(player_room, direction)
                
    def player_look(self):
        #this stuff will be in character.py class soon(hopefully)
        player_descripions = [ #just add more descriptions here for more randomness
            'looking fresh as ever',
            'very heroic looking',
            'according to grandma, you are a real cutie. i think otherwise',
            'id rather not...'
            ]
        print()
        type_effect(choice(player_descripions))

    def go(self, player_room):
        player.room = player_room
        
    def get_room_items(self, player_room = False):
        print()
        type_effect('You can see ')
        x = 0
        for i in Object.instances:
            if not player_room:
                if i.room == self.name:
                    if i.parent == 'void':
                        if x == 0:
                            type_effect(i.longName)
                            x += 1
                        else:
                            type_effect(f', {i.longName}')
                            x += 1
                    else:
                        if i.get_parent_open(i.parent):
                            if x == 0:
                                type_effect(i.longName)
                                x += 1
                            else:
                                #debug(i.longName)
                                type_effect(f', {i.longName}')
                                x += 1
            else:
                if i.room == player_room:
                    if i.parent == 'void':
                        if x == 0:
                            type_effect(i.longName)
                            x += 1
                        else:
                            type_effect(f', {i.longName}')
                            x += 1
                    else:
                        if i.get_parent_open(i.parent):
                            if x == 0:
                                type_effect(i.longName)
                                x += 1
                            else:
                                #debug(i.longName)
                                type_effect(f', {i.longName}')
                                x += 1
        if x == 0:
            print()
            type_effect('nothing...')

    def room_description(self, player_room, moved = False):
        for i in Room.instances:
            if i.name == player_room:
                print()
                if moved == True:
                    print('-----------------------------------------------------------------------------------------------')
                type_effect(i.description)
                i.get_room_items(player_room)
                i.get_room_directions()
                    
    def get_room_directions(self):
        print()
        type_effect('You can go:')
        x = 0
        if self.north != False:
            print()
            type_effect('north')
            x += 1
        if self.south != False:
            print()
            type_effect('south')
            x += 1
        if self.east != False:
            print()
            type_effect('east')
            x += 1
        if self.west != False:
            print()
            type_effect('west')
            x += 1
        if x == 0:
            print()
            type_effect('nowhere...')

    def move_room(self, player_room, direction):
        for i in Room.instances:
            if i.name == player.room:
                if direction == 'north':
                    if i.north != False:
                        player.room = i.north
                        print()
                        type_effect('You have moved North')
                        i.room_description(player.room)
                
                if direction == 'south':
                    if i.south != False:
                        player.room = i.south
                        print()
                        type_effect('You have moved South')
                        i.room_description(player.room)

                if direction == 'east':
                    if i.east != False:
                        player.room = i.east
                        print()
                        type_effect('You have moved East')
                        i.room_description(player.room)

                if direction == 'west':
                    if i.west != False:
                        player.room = i.west
                        print()
                        type_effect('You have moved West')
                        i.room_description(player.room)

    def change_room(self, player_room):
        player.room = player_room

    def set_directions(self, north = False, south = False, east = False, west = False):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def change_description(self, description = 'void'):
        self.description = description