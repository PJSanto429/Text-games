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

def text_input(text, player_room = 'none', version = 'main'): #pretty much done
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
            if version == 'dev' or version == 'main':
                saveGame(player_room)
            #elif version == 'main':
                #print()
                #type_effect('Sorry, the save function is currently unavailable. Please try again in a later version of the game.')

        elif action == 'load':
            if version == 'dev' or version == 'main':
                player_room = loadGame()
                room.go(player_room)
                room.action('look', player_room) #cleaned up a lot

            #elif version == 'main':
                #print()
                #type_effect('Sorry, the load function is currently unavailable. Please try again in a later version of the game.')

        elif action == 'take' or action == 'drop' or (action == 'look' or action == 'l'):
            x = 0
            for i in Object.instances:
                if i.longName in fullText:
                    i.fullName_action(action, i.longName, player_room)
                    x = 1
            if x == 0:
                thing.action(action, text[x - 1], player_room)

        #elif action in action.list:
            #do something
    
    except:
        pass