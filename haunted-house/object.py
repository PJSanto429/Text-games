from random import randint

from typeEffect import type_effect
from debugger import debug

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
            self.room = 'inventory'
        #----------------------------------
        self.isContainer = False
        self.containerKey = 'none'
        self.containerLimit = 'none'
        self.containerLocked = False
        #----------------------------------
        self.otherActions = {}
        self.aliases = []
        self.parent = parent #will be used for things like fridges, chests, etc.
        self.health = health        #Health and money will be set to 0 as a default
        self.money = money          #most items will not have health or money

        self.takeable_message = 'void'
        self.cantSee = "Hmm, I can't see that"
        self.noDesc = "I see nothing out of the ordinary..."

    def add_attribute(self, attribute = 'void', description = 'void', action = 'none', inventoryNeed = False, locked = False):
        if attribute not in Object.otherActions:
            Object.otherActions.append(attribute)
        self.otherActions.update({attribute: f'{description}|{action}|{inventoryNeed}|{locked}'})
        
    def add_aliases(self, aliases: list):
        for alias in aliases:
            if alias not in self.aliases:
                self.aliases.append(alias)
        
    def put_into_input_sorter(self, fullText, player_room):
        fullText = fullText.replace('put ', '')
        text = fullText.split('into')
        text[0], text[1] = text[0].strip(), text[1].strip()
        item, container = False, False
        itemName, containerName = False, False
        for i in Object.instances:
            if text[1] == i.longName:
                container = i
            elif i.name in text[1]:
                containerName = i.name
            if text[0] == i.longName:
                item = i
            elif i.name in text[0]:
                itemName = i.name
        if type(item) == Object and type(container) == Object:
            item.put_into_container(container)
        elif type(item) == Object and not type(container) == Object:
            self.put_into_sorter(player_room, item, containerName)
        elif not type(item) == Object and type(container) == Object:
            self.put_into_sorter(player_room, itemName, container)
        else:
            self.put_into_sorter(player_room, itemName, containerName)
            
    def drop_input_sorter(self, player_room):
        inventory = []
        for i in Object.instances:
            if i.inInventory:
                inventory.append(i)
        item = self.ask_items(inventory, 'You don\'t have that', False, 'Which item would you like to drop?')
        for i in item:
            i.pick_drop('drop', player_room)
            
    def take_input_sorter(self, player_room):
        itemList = []
        for i in Object.instances:
            if i.room == player_room and i.takeable and not i.inInventory:
                if i.parent == 'void' or (i.get_parent_open(i.parent)):
                    itemList.append(i)
        item = self.ask_items(itemList, False, False, 'Which item would you like to take?')
        for i in item:
            i.pick_drop('take', player_room)
        
    
    def action_input_sorter(self, action, player_room, text, fullText):
        x = 0
        actions = ['take ', 'pick ', ' up ', 'drop ', 'look ', 'examine', 'at ']
        for word in Object.otherActions:
            actions.append(f'{word} ')
        for word in actions:
            if word in fullText:
                fullText = fullText.replace(word, '')
        fullText = fullText.strip()
        for i in Object.instances:
            if i.longName == fullText:
                i.fullName_action(action, i.longName, player_room)
                x = 1
        if x == 0:
            self.action(action, fullText, player_room)
    
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
            items = []
            print()
            for i in Object.instances:
                if len(items) <= 3:
                    item = (Object.instances[randint(0, len(Object.instances) - 1)])
                    if item.longName != 'void' and item.takeable and i.parent == 'void' and item not in items:
                        print() #add the item to a list so it only prints it once
                        type_effect(item.longName)
                        items.append(item)

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
        #add the item long name to be printed above the description
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
                elif action in ['look', 'l', 'examine']:
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
            if container.isContainer and container.open:
                if type(container.containerLimit) == int:
                    amount = 0
                    for x in Object.instances:
                        if x.parent == container.longName:
                            amount += 1    
                    if container.containerLimit > amount:
                        self.parent = container.longName
                        self.inInventory = False
                        self.room = container.room
                        type_effect(f'you put {self.longName} into {container.longName}')
                    elif container.containerLimit == x:
                        print()
                        type_effect(f'There are already {container.containerLimit} items in {container.longName}')
                else:
                    print()
                    type_effect(f'you put {self.longName} into {container.longName}')
                    self.parent = container.longName
                    self.inInventory = False
                    self.room = container.room
            elif container.isContainer and not container.open:
                print()
                type_effect(f'{container.longName} is closed. would you like to try and open it? ')
                choice = input().lower()
                if choice in yes:
                    if container.open_close('open'):
                        self.put_into_container(container)
                else:
                    print()
                    type_effect('ok, maybe later')
            elif not container.isContainer:
                print()
                type_effect(f'You cannot put {self.longName} into {container.longName}')
        else:
            print()
            type_effect(f'You cannot do that to {self.longName}')
       
    def ask_items(self, objects, falseMessage = False, sayInventory = False, askMessage = False):
        if len(objects) == 0:
            print()
            type_effect(self.cantSee)
            return False
        if len(objects) == 1:
            print()
            return([objects[0]])
        if len(objects) > 1:
            print()
            if not askMessage:
                type_effect('which did you mean?')
            else:
                type_effect(askMessage)
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
        if type(objectName) != Object:
            for i in Object.instances:
                if i.name == objectName and ((i.room == player_room and i.get_parent_open(i.parent)) or i.inInventory):
                    objects.append(i)
            item = self.ask_items(objects)[0]
        else:
            item = objectName
        
        if type(containerName) != Object:
            for x in Object.instances:
                if x.room == player_room and x.name == containerName and x.isContainer:
                    containers.append(x)
            container = self.ask_items(containers)[0]
        else:
            container = containerName
        #now to actually go into the container
        item.put_into_container(container)
            
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

    def alias_check(self, name):
        for alias in self.aliases:
            if alias == name:
                return True
    
    def action(self, action, name, player_room = 'none'):
        itemList = []
        for i in Object.instances:
            if i.name == name or i.alias_check(name):
                if (i.room == player_room or i.inInventory):
                    if i.parent == 'void' or (i.get_parent_open(i.parent)):
                        itemList.append(i)
                    
        if action == 'drop':
            inventory = []
            for i in Object.instances:
                if i.name == name and i in itemList:
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

        elif action in ['look', 'examine'] or action in Object.otherActions:
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
                        type_effect(f"You have picked up the {self.longName}")
                        print()
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
                    type_effect(f"You have dropped {self.longName}")
            else:
                print()
                type_effect(f"You don't have {self.longName} in your inventory")

    def return_name(self, x = 'name'):
        if x == 'name':
            return self.name
        elif x == 'longName':
            return self.longName