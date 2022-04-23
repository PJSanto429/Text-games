import sys
from time import sleep
from main import *

class Object: #DOESN'T WORK     GARBAGE
    def __init__(self, name, description = 'void', health = 0, money = 0, code = 000, takeable = False, inInventory = False, room = 'void'):
        self.name = name #mandatory
        self.description = description #mandatory
        self.health = health        #Health and money will be set to 0 as a default
        self.money = money          #
        self. code = code  #for items that might be special. most will be 000
        self.takeable = takeable #lets items be picked up. default will be False(unable to be picked up)
        self.inInventory = inInventory  #this will always be false by default
        self.room = room #default is void(kind of a storage area)

    def item_description(self):
        if self.description == 'void':
            pass
        if player_room == self.room:
            print()
            type_effect(self.description)

    def add_descrition(self, description):
        self.description = description
    
    def test(self):
        print()
        type_effect(f"Name: {self.name}")
        print()
        type_effect(f"Description: {self.description}")
        print()
        type_effect(f"Health: {self.health}")
        print()
        type_effect(f"Money: {self.money}")
        print()
        type_effect(f"Code: {self.code}")
        print()
        type_effect(f"Takeable: {self.takeable}")
        print()
        type_effect(f"inInventory: {self.inInventory}")
        print()
        type_effect(f"Room: {self.room}")