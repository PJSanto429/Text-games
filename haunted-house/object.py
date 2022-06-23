'''Object class. as of date on main.py, it is UNFINISHED'''

import sys
from time import sleep
from random import randint, choice
import gc
from typeEffect import type_effect
from debugger import debug

player_inventory = []

yes = ['yes', 'y']
no = ['no', 'n']

#room inventories:  #i don't think i will need these 
void_INV = []
starting_room_INV = [] #these are not going to end up in the 'final' product, currently being used for testing 
RM_1_INV = []
#item_list = starting_room_INV + RM_1_INV

class Object: #unfinished - main priority
    instances = []
    otherActions = []
    #name, player_room, room, description, takeable, inInventory #this is the most basic stuff
    def __init__(self, name = 'void', room = 'start', description = 'void', takeable = False, inInventory = False, longName = 'void', parent = 'void', open = False, hidden = False, seen = False, health = 0, money = 0):
        self.__class__.instances.append(self)
        self.name = name #gives name to object(default is 'void')
        self.room = room #default is void(kind of a storage area)
        self.homeRoom = room #this is going to work as a way to reset objects when saving and loading
        self.open = open
        self.isContainer = False
        if self.open == False:
            self.description = description #mandatory
            self.closedDescription = description
            self.openDescription = 'void' #this will need to be set
        elif self.open == True:
            self.description = description
            self.closedDescription = 'void'
            self.openDescription = description
        self.takeable = takeable #lets items be picked up. default will be False(unable to be picked up)
        self.inInventory = inInventory  #this will always be false by default
        self.longName = longName #for if there are multiple items in room/inventory with same name
        self.seen = seen #for checking if the object has been seen(not currently being used)
        if self.inInventory == True:
            player_inventory.append(self.longName)
            self.room = 'inventory'
        self.otherActions = {}
        self.parent = parent #will be used for things like fridges, shests, etc.
        self.health = health        #Health and money will be set to 0 as a default
        self.money = money          #most items will not have health or money

        self.takeable_message = 'void'
        self.cantSee = "Hmm, I can't see that"
        self.noDesc = "I see nothing out of the ordinary..."

    def add_attribute(self, attribute = 'void', description = 'void', action = 'none', inventoryNeed = False, locked = False):
        Object.otherActions.append(attribute)
        self.otherActions.update({attribute: f'{description}|{action}|{inventoryNeed}|{locked}'})

    def see_open_message(self):
        for i in Object.instances: #wow this is cool
            if i.name == 'fridge1':
                return i.open_message
    
    def open_close(self, action, message = 'none'):
        if action == 'open':
            if self.open == False:
                self.open = True
                self.description = self.openDescription
                print()
                type_effect(message)
            else:
                print()
                type_effect(f'{self.longName} is already open')

        if action == 'close':
            if self.open == True:
                self.open = False
                self.description = self.closedDescription
                print()
                type_effect(message)
            else:
                print()
                type_effect(f'{self.longName} is already closed')
            
    def see_inventory(self):
        inv = 0
        print()
        type_effect('Your inventory consists of:')
        for i in Object.instances:
            if i.inInventory == True:
                inv += 1
                print()
                type_effect(i.longName)
        if inv == 0:
            print()
            type_effect('Nothing yet...')

    def other_action(self, name, action):
        for i in Object.instances:
            if i.longName == name:
                if action in i.otherActions:
                    x = i.otherActions[action]
                    x = x.split('|')
                    if x[1] == 'open' or x[1] == 'close':
                        i.open_close(x[1], x[0])
                    else:
                        print()
                        type_effect(x[0])
                else:
                    print()
                    type_effect(f"You can't do that to the {i.longName}")

    def get_parent_open(self, parent): #this is used for making sure that an object's parent is open
        for i in Object.instances:
            if i.longName == parent and i.open == True:
                return True

    def item_description(self): #prints the item's description
        if self.description == 'void':
            print()
            type_effect(self.noDesc)
        else:
            print()
            type_effect(self.description)
            self.seen = True

    def notTakeable_message(self, message):
        #this is for adding more variety to the game => instead of just saying 'you cant take that', it would say 'this is too heavy to take
        if message == 'heavy':
            self.takeable_message = 'This is far to heavy to carry, and you are no weightlifter'
        #add more messages here:
        #elif message == ''
        else:
            self.takeable_message = message

    def fullName_action(self, action, name, player_room):
        if self.room == player_room or self.inInventory == True and (self.parent == 'void' or (self.get_parent_open(self.parent))):
            if self.parent == 'void' or (self.get_parent_open(self.parent)):
                if action == 'take' or action == 'drop':
                    self.pick_drop(action, player_room)
                elif action == 'look':
                    self.item_description()
                else:
                    self.other_action(name, action)
       
            else:
                print()
                type_effect("Hmm, I can't see that")
        else:
            print()
            type_effect("Hmm, I can't see that")

    def create_container(self, itemLimit = 'none'):
        self.isContainer = True
        self.containerLimit = itemLimit

    def put_into_container(self, container):
        if self.takeable == True:
            for i in Object.instances:
                if i.longName == container and i.isContainer:
                    x = 0
                    for x in Object.instances:
                        if x.parent == i.longName:
                            x += 1
                    if i.containerLimit > x:
                        self.parent = i.longName
                        print(self.parent)
                    elif i.containerLimit == x:
                        print()
                        type_effect(f'There are already {i.containerLimit} items in {i.longName}')
                elif i.longName == container and not i.isContainer:
                    print()
                    type_effect(f'You cannot put {self.longName} into {i.longName}')

    def action(self, action, name, player_room = 'none'):
        itemList = []
        
        for i in Object.instances:
            if i.name == name and (i.room == player_room or i.inInventory == True):
                if i.parent == 'void' or (i.get_parent_open(i.parent)):
                    itemList.append(i.longName)

        if len(itemList) == 0:
            print()
            type_effect(self.cantSee)

        elif len(itemList) == 1:
            for i in Object.instances:
                if i.name == name:
                    if i.room == player_room or i.inInventory == True:
                        if action == 'take' or action == 'drop':
                            i.pick_drop(action, player_room)
                        if action == 'look':
                            i.item_description()
                        if action in Object.otherActions:
                            i.other_action(i.longName, action)

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
                roomInventory = []
                for i in Object.instances:
                    if i.longName in itemList and i.inInventory == False:
                        roomInventory.append(i.longName)
                        x += 1

                if len(roomInventory) > 1:
                    print()
                    type_effect(f'Which did you mean?  ')
                    for i in roomInventory:
                        print()
                        type_effect(i)

                    print()
                    choice = input()
                    print()
                    for i in Object.instances:
                        if (i.longName == choice) and (i.inInventory == False) and (i.longName in roomInventory):
                            i.pick_drop(action, player_room)
                            x = True

                    if x != True:
                        print()
                        type_effect(self.cantSee)
                
                elif len(roomInventory) == 1:
                    for i in Object.instances:
                        if i.longName in itemList and i.inInventory == False:
                            #print()
                            #type_effect(i.longName)
                            i.pick_drop(action, player_room)

            elif action == 'look' or action in Object.otherActions:
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
                        if action == 'look':
                            i.item_description()
                        else:
                            i.other_action(i.longName, action)
                        x = True
                if x != True:
                    print()
                    type_effect(self.cantSee)

    def change_name(self, nameType, name): #name type is which name are you changing(name or longName)
        if nameType == 'longName':
            self.longName = name
        if nameType == 'name':
            self.name = name

    def change_room(self, room):
        self.room = room

    def change_description(self, description):
        self.description = description
    
    def open_description(self, description):
        self.openDescription = description

    def closed_description(self, description):
        self.closedDescription = description

    def change_takeable(self, takeable = False): #either True or False
        self.takeable = takeable

    def pick_drop(self, action, player_room, inform = True): #either 'take' or 'drop'; WILL BE USED  A LOT
        if action == 'take':
            if self.takeable == True:
                if self.inInventory == True: #checks to see if the item is already in the player inventory
                    if inform:
                        print()
                        type_effect(f"You already have {self.longName} in your inventory")
                elif self.inInventory == False:
                    self.inInventory, self.room, self.parent = True, 'inventory', 'void'
                    #self.room = 'inventory'
                    #self.parent = ''
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
                    type_effect(f"You have dropped {self.longName}")
                else:
                    player_inventory.remove(self.longName)
            elif self.inInventory == False:
                print()
                type_effect(f"You don't have {self.longName} in your inventory")

    def return_name(self, x = 'name'):
        if x == 'name':
            return self.name
        elif x == 'longName':
            return self.longName