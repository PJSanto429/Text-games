'''Object class. as of date on main.py, it is UNFINISHED'''

import sys
from time import sleep
from random import randint, choice

player_inventory = []

#room inventories:  #i don't think i will need these 
void_INV = ['chair','cat']
starting_room_INV = [] #these are not going to end up in the 'final' product, currently being used for testing 
RM_1_INV = []
#item_list = starting_room_INV + RM_1_INV

def type_effect(text = ""): #typewriter effect. idk how it works
    words = text
    for char in words:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

class Object: #unfinished - main priority
    #name, player_room, room, description, takeable, inInventory
    def __init__(self, name = 'void', player_room = void_INV, room = void_INV, description = 'void', takeable = False, inInventory = False, longName = 'void', genre = 'none', code = .0000, health = 0, money = 0):
        self.name = name #mandatory
        self.player_room = player_room
        self.room = room #default is void(kind of a storage area)
        #self.room.append(self.name)
        #self.room.append(self.name)  #doesn't work. IDK if it is needed
        self.description = description #mandatory
        self.takeable = takeable #lets items be picked up. default will be False(unable to be picked up)
        self.inInventory = inInventory  #this will always be false by default
        if self.inInventory:
            player_inventory.append(self.name)
        self.longName = longName
        self. code = code  #for items that might be special. most will be 000
        self.health = health        #Health and money will be set to 0 as a default
        self.money = money          #

        self.takeable_message = 'void'
        self.cantSee = "Hmm, I can't see that"
        self.noDesc = "I see nothing special about that"

    def inventory_change(self, action):
        if action == 'drop':

            if self.room == 'void':
                void_INV.append(self.name)
            elif self.room == 'start':
                starting_room_INV.append(self.name)

        if action == 'take':
            pass

    def item_description(self):
        if self.description == 'void':
            print()
            type_effect(self.noDesc)

        else:
            print()
            type_effect(self.description)

    def notTakeable_message(self, message):
        self.takeable_message = message
        '''print()      #these two lines were simply for testing
        type_effect(f'take message has been changed to {self.takeable_message}')'''

    def action(self, action):  #redirects the code to either item_description or take_drop
        if action == 'take' or action == 'drop':
            self.pick_drop(action)
        elif action == 'look':
            self.item_description()

    def change_name(self, name):
        self.name = name

    def change_room(self, room):
        self.room = room

    def change_description(self, description):
        self.description = description

    def change_takeable(self, takeable): #either True or False
        self.takeable = takeable

    def pick_drop(self, action, inform=True): #either 'take' or 'drop'; WILL BE USED  A LOT
        if action == 'take':
            if self.takeable == True:

                if self.inInventory == True: #checks to see if the item is already in the player inventory
                    if inform:
                        print()
                        type_effect(f"You already have {self.name} in your inventory")
                elif self.inInventory == False:
                    self.inInventory = True
                    if inform:
                        print()
                        player_inventory.append(self.name)

                        type_effect(f"You have picked up {self.name}")

            elif self.takeable == False:
                if self.takeable_message != 'void':
                    print()
                    type_effect(self.takeable_message)
                else:
                    print()
                    type_effect("Despite your best attempts, you are unable to pick this up")

        if action == 'drop':
            if self.inInventory == True:
                self.inInventory = False
                if inform:
                    print()
                    player_inventory.remove(self.name)
                    type_effect(f"You have dropped {self.name}")
            elif self.inInventory == False:
                if inform:
                    print()
                    type_effect(f"You don't have {self.name} in your inventory")

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