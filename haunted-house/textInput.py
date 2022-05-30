#text input

from typeEffect import type_effect
from object import Object, player_inventory
from room import *
from saveGame import *

#constants:
cantSee = "Hmm, I can't see that"
noDesc = "I see nothing special about that"

#these two are kind of like windows into the Object and Room classes, avoids the need for more imports
thing = Object('void', 'none')
room = Room()

def text_input(text, player_room='none'): #pretty much done
    text = text.lower()
    fullText = text
    text = text.split()
    try:
        action = text[0]
        x = len(text)

        if text[0] == 'quit' or text[0] == 'quit()' or text[0] == 'stop':
            print()
            #type_effect('Would you like to save ') #work on this more(4C)

            type_effect('Quitting...')
            quit()

        elif action =='inv' or action == 'inventory' or action == 'i':
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

        elif action == 'wait':
            print()
            type_effect('Time passes...')
        
        elif len(text) == 1 and (action == 'look' or action == 'l'):
            room.action('look', player_room)

        elif action == 'move' or action == 'go':
            room.action('move', player_room, text[x - 1])

        elif action == 'save':
            saveGame(player_room)

        elif action == 'load':
            player_room, inventory = loadGame()
            #player_room = getRoom(code)
            room.go(player_room)

            #inventory = getInventory(code)
            for i in Object.instances:
                if i.longName in inventory:
                    i.inInventory = True
                    i.room = 'inventory'
                    player_inventory.append(i.longName)
                else:
                    i.inInventory = False
                    try:
                        player_inventory.remove(i.longName)
                    except:
                        pass

            room.action('look', player_room)

        elif action == 'take' or action == 'drop' or action == 'look':
            x = 0
            for i in Object.instances:
                if i.longName in fullText:
                    i.fullName_action(action, i.longName, player_room)
                    x = 1
            if x == 0:
                thing.action(action, text[x - 1], player_room)
    
    except:
        pass