import sys
from time import sleep
from main import *

class Object: #unfinished - main priority
    #name, player_room, description, room, takeable
    def __init__(self, name, player_room = 'void', room = 'void', description = 'void', takeable = False, inInventory = False, health = 0, money = 0, code = 000):
        self.name = name #mandatory
        self.player_room = player_room
        self.description = description #mandatory
        self.health = health        #Health and money will be set to 0 as a default
        self.money = money          #
        self. code = code  #for items that might be special. most will be 000
        self.takeable = takeable #lets items be picked up. default will be False(unable to be picked up)
        self.inInventory = inInventory  #this will always be false by default
        self.room = room #default is void(kind of a storage area)

        self.cantSee = "Hmm, I can't see that"
        self.noDesc = "I see nothing special about that"

    def item_description(self):
        if self.player_room == self.room:

            if self.description == 'void':
                print()
                type_effect(self.noDesc)

            else:
                print()
                type_effect(self.description)

        else:
            print
            type_effect(self.cantSee)

    def add_descrition(self, description):
        self.description = description

    def change_room(self, room):
        self.room = room

    def change_descriptino(self, desccription):
        self.description = desccription
    
    def test(self): #prints all item descriptions
        print()
        type_effect(f"Name: {self.name}")
        print()
        type_effect(f"Player Room: {self.player_room}")
        print()
        type_effect(f"Room: {self.room}")
        print()
        type_effect(f"Description: {self.description}")
        print()
        type_effect(f"Takeable: {self.takeable}")
        print()
        type_effect(f"inInventory: {self.inInventory}")
        print()
        type_effect(f"Health: {self.health}")
        print()
        type_effect(f"Money: {self.money}")
        print()
        type_effect(f"Code: {self.code}")