import sys
from time import sleep
from main import *

class Object: #unfinished - main priority
    #name, player_room, description, room, takeable
    def __init__(self, name = 'void', player_room = 'void', room = 'void', description = 'void', takeable = False, inInventory = False, health = 0, money = 0, code = 000):
        self.name = name #mandatory
        self.player_room = player_room
        self.room = room #default is void(kind of a storage area)
        #self.room.append(self.name)  #doesn't work. IDK if it is needed
        self.description = description #mandatory
        self.takeable = takeable #lets items be picked up. default will be False(unable to be picked up)
        self.inInventory = inInventory  #this will always be false by default
        self.health = health        #Health and money will be set to 0 as a default
        self.money = money          #
        self. code = code  #for items that might be special. most will be 000

        self.cantSee = "Hmm, I can't see that"
        self.noDesc = "I see nothing special about that"

    def item_description(self, player_room, room):
        self.player_room = player_room
        self.room = room
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

    def change_name(self, name):
        self.name = name

    def change_room(self, room):
        self.room = room

    def change_description(self, description):
        self.description = description

    def is_takeable(self, takeable): #either True or False
        self.takeable = takeable

    def pick_drop(self, action): #either 'take' or 'drop'; WILL BE USED  A LOT
        if action == 'take':
            if self.inInventory == True: #checks to see if the 
                print()
                type_effect(f"You already have {self.name} in your inventory")
            else:
                self.inInventory = True
                print()
                type_effect(f"You have picked up {self.name}")

        if action == 'drop':
            if self.inInventory == True:
                self.inInventory = False
                print()
                type_effect(f"You have dropped {self.name}")
            else:
                print()
                type_effect(f"You don't have{self.name} in your inventory")
        #self.inInventory = inInventory

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