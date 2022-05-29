'''Object class. as of date on main.py, it is UNFINISHED'''

import sys
from time import sleep
from random import randint, choice
import gc
from typeEffect import type_effect

player_inventory = []

yes = ['yes','y']
no = ['no','n']

#room inventories:  #i don't think i will need these 
void_INV = []
starting_room_INV = [] #these are not going to end up in the 'final' product, currently being used for testing 
RM_1_INV = []
#item_list = starting_room_INV + RM_1_INV

class Object: #unfinished - main priority
    instances = []
    #name, player_room, room, description, takeable, inInventory
    def __init__(self, name = 'void', room = 'start', description = 'void', takeable = False, inInventory = False, longName = 'void', seen = False, health = 0, money = 0, parent = 'object', code = .0000):
        self.__class__.instances.append(self)
        self.name = name #gives name to object(default is 'void')
        self.room = room #default is void(kind of a storage area)
        self.description = description #mandatory
        self.takeable = takeable #lets items be picked up. default will be False(unable to be picked up)
        self.inInventory = inInventory  #this will always be false by default
        self.longName = longName #for if there are multiple items in room/inventory with same name
        self.seen = seen #for checking if the object has been seen
        if self.inInventory == True:
            player_inventory.append(self.longName)
        self.parent = parent
        self.code = code  #for items that might be special. most will be 000
        self.health = health        #Health and money will be set to 0 as a default
        self.money = money          #most items will not have health or money

        self.takeable_message = 'void'
        self.cantSee = "Hmm, I can't see that"
        self.noDesc = "I see nothing special about that"

        if self.room == 'start':
            starting_room_INV.append(self.longName)
        if self.room == 'room1':
            RM_1_INV.append(self.longName)
        
    def inventory_change(self, action): #i think that this changes what room/inventory this is in
        if action == 'drop':

            if self.room == 'void':
                void_INV.append(self.name)
            elif self.room == 'start':
                starting_room_INV.append(self.name)

        if action == 'take':
            pass

    def add_attribute(self, attribute = 'void', description = 'void', locked = False):
        self.locked = locked
        if attribute == 'read':
            self.read = description

    def item_description(self): #prints the item's description
        if self.description == 'void':
            print()
            #type_effect('this is cool')
            type_effect(self.noDesc)

        else:
            print()
            type_effect(self.description)
            self.seen = True
            if self.name == 'note':
                print()
                type_effect('Would you like to read note? ')
                print()
                choice = input()
                if choice in yes:
                    if self.locked == False:
                        print()
                        type_effect('The note reads: ')
                        print()
                        type_effect(self.read)
                    elif self.locked == True:
                        print()
                        type_effect('Despite your best attempts, you are unable to read this. It must be in another language or something...')
                elif choice in no:
                    print()
                    type_effect('Ok, your loss')

    def notTakeable_message(self, message):
        #this is for adding more variety to the game => instead of just saying 'you cant take that', it would say 'this is to heavy to take
        if message == 'heavy':
            self.takeable_message = 'This is far to heavy to carry, and you are no weightlifter'
        #add more messages here:
        #elif message == ''
        else:
            self.takeable_message = message

        #these two lines were simply for testing:
        '''print()
        type_effect(f'take message has been changed to {self.takeable_message}')'''

    def fullName_action(self, action, name, player_room):
        if self.room == player_room or self.inInventory == True:
            if action == 'take' or action == 'drop':
                self.pick_drop(action, player_room)    
            elif action == 'look':
                self.item_description()
            else:
                print()
                type_effect('Thats not a verb I recognize')
        else:
            print()
            type_effect("Hmm, I can't see that")
       
    def action(self, action, name, player_room = 'none'):
        itemList = []
        
        for i in Object.instances:
            if i.name == name and (i.room == player_room or i.inInventory == True):
                itemList.append(i.longName)

        if len(itemList) == 0:
            print()
            type_effect(self.cantSee)

        elif len(itemList) == 1:
            for i in Object.instances:
                if i.name == name:

                    if i.name == name and i.room == player_room and i.inInventory == False:
                        if action == 'take':
                            i.pick_drop(action, player_room)
                        if action == 'look':
                            i.item_description()

                    elif i.name == name and i.inInventory == True:
                        if action == 'drop':
                            i.pick_drop(action, player_room)
                        elif action == 'look':
                            i.item_description()

                    '''if i.name == name and (i.room == player_room or i.inInventory == True):
                        if action == 'take' or action == 'drop':
                            i.pick_drop(action, player_room)
                        elif action == 'look':
                            i.item_description()
                        else:
                            print()
                            type_effect('Thats not a verb I recognize')'''

        elif len(itemList) > 1:

            if action == 'drop':
                x = 0
                inventory = []
                for i in Object.instances:
                    if i.inInventory == True:
                        inventory.append(i.longName)
                        x += 1

                if len(inventory) > 1:
                    print()
                    type_effect(f'Which did you mean?  ')
                    for i in inventory:
                        print()
                        type_effect(i)

                    print()
                    choice = input()
                    print()
                    for i in Object.instances:
                        if (i.longName == choice) and (i.inInventory == True) and (i.longName in inventory):
                            i.pick_drop(action, player_room)
                            x = True

                    if x != True:
                        print()
                        type_effect("You don't have that!")
                
                elif len(inventory) == 1:
                    for i in Object.instances:
                        if i.longName in itemList and i.inInventory == True:
                            i.pick_drop(action, player_room)

            elif action == 'take':
                x = 0
                inventory = []
                for i in Object.instances:
                    if i.longName in itemList and i.inInventory == False:
                        inventory.append(i.longName)
                        x += 1

                if len(inventory) > 1:
                    print()
                    type_effect(f'Which did you mean?  ')
                    for i in inventory:
                        print()
                        type_effect(i)

                    print()
                    choice = input()
                    print()
                    for i in Object.instances:
                        if (i.longName == choice) and (i.inInventory == False) and (i.longName in inventory):
                            i.pick_drop(action, player_room)
                            x = True

                    if x != True:
                        print()
                        type_effect(self.cantSee)
                
                elif len(inventory) == 1:
                    for i in Object.instances:
                        if i.longName in itemList and i.inInventory == False:
                            #print()
                            #type_effect(i.longName)
                            i.pick_drop(action, player_room)

            elif action == 'look':
                x = 0
                inventory = []
                print()
                type_effect(f'Which did you mean?  ')
                for i in Object.instances:
                    if i.longName in itemList and i.inInventory == True:
                        print()
                        type_effect(f"{i.longName} - inventory")
                        inventory.append(i.longName)
                        x += 1
                    elif i.longName in itemList and i.room == player_room:
                        print()
                        type_effect(i.longName)

                print()
                choice = input()
                print()
                for i in Object.instances:
                    if i.longName == choice and (i.longName in itemList) and (i.inInventory == True or i.room == player_room):
                        #print()
                        #type_effect(i.longName)
                        i.item_description()
                        x = True
                if x != True:
                    print()
                    type_effect(self.cantSee)

    def change_name(self, name):
        self.name = name

    def different_actions(self, action):
        if action == 'read':
            pass

    def change_room(self, room):
        self.room = room

    def change_description(self, description):
        self.description = description

    def change_takeable(self, takeable): #either True or False
        self.takeable = takeable

    def pick_drop(self, action, player_room, inform=True): #either 'take' or 'drop'; WILL BE USED  A LOT
        if action == 'take':
            if self.takeable == True:
                if self.inInventory == True: #checks to see if the item is already in the player inventory
                    if inform:
                        print()
                        type_effect(f"You already have {self.name} in your inventory")
                elif self.inInventory == False:
                    self.inInventory = True
                    self.room = 'inventory'
                    if inform == True:
                        print()
                        player_inventory.append(self.longName)
                        type_effect(f"You have picked up the {self.longName}")
                        print()
                    elif inform == False:
                        player_inventory.append(self.longName)
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
                self.room = player_room
                if inform == True:
                    print()
                    player_inventory.remove(self.longName)
                    type_effect(f"You have dropped {self.name}")
                else:
                    player_inventory.remove(self.longName)
            elif self.inInventory == False:
                print()
                type_effect(f"You don't have {self.name} in your inventory")

    def return_name(self, x = 'name'):
        if x == 'name':
            return self.name
        elif x == 'longName':
            return self.longName

    def test(self, action='all'): #default action is to print all item description
        if action == 'all':
            print()
            type_effect(f"Name: {self.name}")
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
        
        if action == 'every':
            for i in Object.instances:
                print()
                type_effect(i.longName)