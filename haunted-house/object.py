from random import randint

from typeEffect import type_effect
from debugger import debug

player_inventory = []

yes = ['yes', 'y']
no = ['no', 'n']

class Object:
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
        if not self.open:
            self.description = description #mandatory
            self.closedDescription = description
            self.openDescription = 'void' #this will need to be set
        elif self.open:
            self.description = description
            self.closedDescription = 'void'
            self.openDescription = description
        #----------------------------------
        self.takeable = takeable #lets items be picked up. default will be False(unable to be picked up)
        self.inInventory = inInventory  #this will always be false by default
        #----------------------------------
        self.longName = longName #for if there are multiple items in room/inventory with same name
        self.seen = seen #for checking if the object has been seen(not currently being used)
        if self.inInventory:
            player_inventory.append(self.longName)
            self.room = 'inventory'
        #----------------------------------
        self.isContainer = False
        self.containerKey = 'none'
        self.containerLimit = 'none'
        self.containerLocked = False
        #----------------------------------
        self.otherActions = {}
        self.parent = parent #will be used for things like fridges, shests, etc.
        self.health = health        #Health and money will be set to 0 as a default
        self.money = money          #most items will not have health or money

        self.takeable_message = 'void'
        self.cantSee = "Hmm, I can't see that"
        self.noDesc = "I see nothing out of the ordinary..."

    def add_attribute(self, attribute = 'void', description = 'void', action = 'none', inventoryNeed = False, locked = False):
        if attribute not in Object.otherActions:
            Object.otherActions.append(attribute)
        self.otherActions.update({attribute: f'{description}|{action}|{inventoryNeed}|{locked}'})
            
    def see_inventory(self, random = False):
        type_effect('Your inventory consists of:')
        if not random:
            inv = 0
            for i in Object.instances:
                if i.inInventory:
                    inv += 1
                    print()
                    type_effect(i.longName)
            if inv == 0:
                print()
                type_effect('Nothing yet...')
        else:
            items = 0
            print()
            for i in Object.instances:
                if items <= 3:
                    item = (Object.instances[randint(0, len(Object.instances) - 1)])
                    if item.longName != 'void' and item.takeable and i.parent == 'void':
                        print() #add the item to a list so it only prints it once
                        type_effect(item.longName)
                        items += 1
                    else:
                        debug(item.longName)
                else:
                    break

    def other_action(self, name, action):
        for i in Object.instances:
            if i.longName == name:
                if action in i.otherActions:
                    x = i.otherActions[action]
                    x = x.split('|')
                    if x[1] in ['open', 'close']:
                        i.open_close(x[1], x[0])
                    elif action in ['lock', 'unlock']:
                        i.lock_unlock_container(action)
                    elif action in ['']: #add move here(to move into another room)
                        pass
                    #also add a way to make the object disappear(just move it into void)
                    else:
                        print()
                        type_effect(x[0])
                else:
                    print()
                    type_effect(f"You can't do that to the {i.longName}")

    def get_parent_open(self, parent): #this is used for making sure that an object's parent is open
        for i in Object.instances:
            if parent != 'void':
                if i.longName == parent and i.open:
                    return True
            else:
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
        #this is for adding more variety to the game => instead of just saying 'you cant take that', it would say 'this is too heavy to take'
        if message == 'heavy':
            self.takeable_message = 'This is far to heavy to carry, and you are no weightlifter'
        #add more messages here:
        #elif message == ''
        else:
            self.takeable_message = message

    def fullName_action(self, action, name, player_room):
        if self.room == player_room or self.inInventory and (self.parent == 'void' or (self.get_parent_open(self.parent))):
            if self.parent == 'void' or (self.get_parent_open(self.parent)):
                if action == 'take' or action == 'drop':
                    self.pick_drop(action, player_room)
                elif action == 'look':
                    self.item_description()
                elif action in ['lock', 'unlock']:
                    self.lock_unlock_container(action)
                else:
                    self.other_action(name, action)
            else:
                print()
                type_effect("Hmm, I can't see that")
        else:
            print()
            type_effect("Hmm, I can't see that")

    def create_container(self, locked = False, key = 'none', lockAbility = False, itemLimit = 'none'):
        self.isContainer = True
        self.locked = locked
        self.containerKey = key
        openAction, closeAction = False, False
        for action in self.otherActions:
            action = action.split('|')
            if action[0] == 'open':
                openAction = True
            if action == 'close':
                closeAction = True
        if not openAction:
            self.add_attribute('open', f'you open {self.longName}', 'open')
        if not closeAction:
            self.add_attribute('close', f'you close {self.longName}', 'close')
        if self.locked:
            self.lockAbility = True
            self.add_attribute('lock')
            self.add_attribute('unlock')
        else:
            self.lockAbility = lockAbility
        self.containerLimit = itemLimit

    def container_check(self, name):
        for i in Object.instances:
            if i.longName == name and i.isContainer:
                return True
    
    def change_container_key(self, key):
        if self.isContainer:
            self.containerKey = key

    def open_close(self, action, message = False):
        if action == 'open':
            if not self.open:
                if self.locked:
                    print()
                    type_effect(f'{self.longName} is locked. Would you like to try and unlock it(y/n)? ')
                    choice = input().lower()
                    if choice in yes:
                        unlocked = self.unlock_container()
                    else:
                        print()
                        type_effect('ok, maybe later')
                else:
                    unlocked = True
                if unlocked:
                    self.open = True
                    self.description = self.openDescription
                    print()
                    if not message:
                        print()
                        type_effect(f'You open {self.longName}')
                    else:
                        type_effect(message)
                    print()
                    type_effect(f'inside of {self.longName}, there is: ')
                    items = 0
                    for i in Object.instances:
                        if i.parent == self.longName:
                            print()
                            type_effect(i.longName)
                            items += 1
                    if items == 0:
                        print()
                        type_effect('nothing...')
                    return True
            else:
                print()
                type_effect(f'{self.longName} is already open')
        if action == 'close':
            if self.open:
                self.open = False
                self.description = self.closedDescription
                print()
                type_effect(message)
            else:
                print()
                type_effect(f'{self.longName} is already closed')

    def lock_unlock_container(self, action):
        if action == 'lock':
            self.lock_container()
        if action == 'unlock':
            self.unlock_container()
    
    def lock_container(self):
        if self.isContainer and self.lockAbility:
            if self.open:
                print()
                type_effect(f'You close {self.longName}')
                self.open = False
            if not self.locked:
                for i in Object.instances:
                    if i.longName == self.containerKey and i.inInventory: #the only way that the container can be locked
                        print()
                        type_effect(f'You have locked {self.longName} with {i.longName}')
                        self.locked = True
                        return True
                    elif i.longName == self.containerKey and not i.inInventory:
                        print()
                        type_effect(f'You do not have the key({self.containerKey}) in your inventory')
                        return False
                    elif i.longName != self.containerKey and i.inInventory:
                        print()
                        type_effect(f'{i.longName} is not the key for {self.longName}')
                        return False
            else:
                print()
                type_effect(f'{self.longName} is already locked')
                    
        else:
            print()
            type_effect(f'You cannot do that to {self.longName}')

    def unlock_container(self):
        if self.isContainer and self.lockAbility:
            if self.locked:
                type_effect(f'what would you like to use to unlock the {self.longName}?(please type the full name) ')
                choice = input().lower()
                longName = False
                for i in Object.instances:
                    if i.longName == choice:
                        longName = True
                        if i.longName == self.containerKey and i.inInventory: #only way that the container can be unlocked
                            print()
                            type_effect(f'You have unlocked {self.longName} with {i.longName}')
                            self.locked = False
                            return True
                        elif i.longName == self.containerKey and not i.inInventory:
                            print()
                            type_effect(f'You do not have the key({self.containerKey}) in your inventory')
                            return False
                        elif i.longName != self.containerKey and i.inInventory:
                            print()
                            type_effect(f'{i.longName} is not the key for {self.longName}')
                            return False

                if not longName:
                    print()
                    type_effect('invalid input')
                    return False
            else:
                print()
                type_effect(f'{self.longName} is not locked')
        else:
            print()
            type_effect(f'You cannot do that to {self.longName}')

    def put_into_container(self, container):
        if self.takeable:
            for i in Object.instances:
                if i.longName == container and i.isContainer and i.open:
                    if type(i.containerLimit) == int:
                        amount = 0
                        for x in Object.instances:
                            if x.parent == i.longName:    
                                amount += 1    
                        if i.containerLimit > amount:
                            self.parent = i.longName
                            self.inInventory = False
                            self.room = i.room
                            type_effect(f'you put {self.longName} into {i.longName}')
                        elif i.containerLimit == x:
                            print()
                            type_effect(f'There are already {i.containerLimit} items in {i.longName}')
                    else:
                        print()
                        type_effect(f'you put {self.longName} into {i.longName}')
                        self.parent = i.longName
                        self.inInventory = False
                        self.room = i.room
                elif i.longName == container and i.isContainer and not i.open:
                    print()
                    type_effect(f'{i.longName} is closed. would you like to try and open it? ')
                    choice = input().lower()
                    if choice in yes:
                        if i.open_close('open'):
                            self.put_into_container(i.longName)
                    else:
                        print()
                        type_effect('ok, maybe later')
                elif i.longName == container and not i.isContainer:
                    print()
                    type_effect(f'You cannot put {self.longName} into {i.longName}')
        else:
            print()
            type_effect(f'You cannot do that to {self.longName}')
       
    def ask_items(self, objects, falseMessage = False, sayInventory = False):
        if len(objects) == 0:
            print()
            type_effect(self.cantSee)
            return False
        if len(objects) == 1:
            print()
            return([objects[0]])
        if len(objects) > 1:
            print()
            type_effect('which did you mean?')
            for i in objects:
                print()
                if sayInventory and i.inInventory:
                    type_effect(f'{i.longName} - inventory')
                else:
                    type_effect(i.longName)
            if len(objects) == 2:
                print()
                type_effect('both')
            elif len(objects) > 2:
                print()
                type_effect('all')
            print()
            choice = input().lower()
            itemGood = False
            if choice in ['both', 'all']:
                itemGood = True
                return objects
            else:
                for i in objects:
                    if i.longName == choice:
                        itemGood = True
                        return [i]
            if not itemGood:
                print()
                if not falseMessage:
                    type_effect(self.cantSee)
                else:
                    type_effect(falseMessage)
            
    def put_into_sorter(self, player_room, objectName, containerName = False):
        objects, containers = [], []
        for i in Object.instances:
            if i.name == objectName and ((i.room == player_room and i.get_parent_open(i.parent)) or i.inInventory):
                objects.append(i)
        for x in Object.instances:
            if x.room == player_room and x.name == containerName and x.isContainer:
                containers.append(x)
                
        item = self.ask_items(objects)
        container = self.ask_items(containers)
        # work on this more(everything after this line needs to be erased/new added)
        #item.put_into_container(container)
        print()
        if item:
            print(f'{item.longName} = {type(item)}')
        else:
            print('no item')
        if container:
            debug(f'{container.longName} = {type(container)}')
        else:
            print('no container')
        #print()
        #type_effect(f'the item you picked is {item.longName}')
        #print('--------------------------------')
        #type_effect(f'the container you picked is {container.longName}')
            
    def get_items(self, name, player_room, takeAbilityNeed = False): # i dont think that this is currently being used: probably delete it
        item_list = []
        for i in Object.instances:
            if i.name == name and (i.room == player_room or i.inInventory):
                if takeAbilityNeed:
                    if i.takeAble:
                        item_list.append(i)
                elif not takeAbilityNeed:
                    item_list.append(i)
        return item_list
    
    def action(self, action, name, player_room = 'none'):
        itemList = []
        for i in Object.instances:
            if i.name == name and (i.room == player_room or i.inInventory):
                if i.parent == 'void' or (i.get_parent_open(i.parent)):
                    itemList.append(i)

        if len(itemList) == 0:
            print()
            type_effect(self.cantSee)

        elif len(itemList) == 1:
            if itemList[0].room == player_room or itemList[0].inInventory:
                if action == 'take' or action == 'drop':
                    itemList[0].pick_drop(action, player_room)
                if action == 'look':
                    itemList[0].item_description()
                if action in Object.otherActions:
                    itemList[0].other_action(itemList[0].longName, action)

        elif len(itemList) > 1:
            if action == 'drop':
                inventory = []
                for i in Object.instances:
                    if i.inInventory:
                        inventory.append(i)
                items = self.ask_items(inventory, 'You don\'t have that!')
                for i in items:
                    i.pick_drop(action, player_room)

            elif action == 'take':
                roomInventory = []
                for i in Object.instances:
                    if i in itemList and not i.inInventory:
                        roomInventory.append(i)
                items = self.ask_items(roomInventory)
                for i in items:
                    i.pick_drop(action, player_room)

            elif action == 'look' or action in Object.otherActions:
                items = self.ask_items(itemList)
                for i in items:
                    if action == 'look':
                        i.item_description()
                    else:
                        i.other_action(i.longName, action)
    
    def open_description(self, description):
        self.openDescription = description

    def closed_description(self, description):
        self.closedDescription = description

    def pick_drop(self, action, player_room, inform = True): #either 'take' or 'drop'; WILL BE USED  A LOT
        if action == 'take':
            if self.takeable:
                if self.inInventory: #checks to see if the item is already in the player inventory
                    if inform:
                        print()
                        type_effect(f"You already have {self.longName} in your inventory")
                else:
                    self.inInventory, self.room, self.parent = True, 'inventory', 'void'
                    if inform:
                        #print()
                        player_inventory.append(self.longName)
                        type_effect(f"You have picked up the {self.longName}")
                        print()
                    else:
                        player_inventory.append(self.longName)
            else:
                if self.takeable_message != 'void':
                    print()
                    type_effect(self.takeable_message)
                else:
                    print()
                    type_effect("Despite your best attempts, you are unable to pick this up")

        if action == 'drop':
            if self.inInventory:
                self.inInventory = False
                self.room = player_room
                if inform:
                    print()
                    player_inventory.remove(self.longName)
                    type_effect(f"You have dropped {self.longName}")
                else:
                    player_inventory.remove(self.longName)
            else:
                print()
                type_effect(f"You don't have {self.longName} in your inventory")

    def return_name(self, x = 'name'):
        if x == 'name':
            return self.name
        elif x == 'longName':
            return self.longName