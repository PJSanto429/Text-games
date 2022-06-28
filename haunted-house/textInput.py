#text input

from typeEffect import type_effect
from object import *
from room import *
from saveGame import *

#constants:
cantSee = "Hmm, I can't see that"
noDesc = "I see nothing special about that"

#these two are kind of like windows into the Object and Room classes, avoids the need for more imports
thing = Object('void', 'none')
room = Room()

def text_input(text, player_room, version = 'main'): #pretty much done
    text = text.lower()
    fullText = text
    text = text.split()
    try:
        action = text[0]
        x = len(text)

        if text[0] == 'quit' or text[0] == 'exit' or text[0] == 'stop':
            quit_save(player_room, version)

        elif action =='inv' or action == 'inventory' or action == 'i':
            thing.see_inventory()

        elif action == 'wait':
            print()
            type_effect('Time passes...')
        
        elif len(text) == 1 and (action == 'look' or action == 'l'):
            room.action('look', player_room)

        elif action == 'move' or action == 'go':
            room.action('move', player_room, text[x - 1])
        
        elif action == 'save':
            saveGame(player_room, version)

        elif action == 'load':
            player_room = loadGame(version)
            room.go(player_room)
            room.action('look', player_room)

        elif action == 'take' or action == 'drop' or (action == 'look' or action == 'l' ) or (action in Object.otherActions):
            x = 0
            for i in Object.instances:
                if i.longName in fullText:
                    i.fullName_action(action, i.longName, player_room)
                    x = 1
            if x == 0:
                thing.action(action, text[x - 1], player_room)

        elif action == 'putinto': # this needs to be worked on
                    #right now all it does is makes sure that the function works properly
            if version == 'dev':
                print()
                type_effect('this function needs to be added(check todo 3.III for an idea of how to do it)...')
                #for i in Object.instances:
                #    if i.longName == 'standard note':
                #        i.put_into_container('gross fridge')

            if version == 'main':
                print()
                type_effect('invalid input.')

        elif action == 'help()':
            if version == 'dev':
                print()
                type_effect('function needs to be added...')
            if version == 'main':
                print()
                type_effect('Sorry, but this function is not available yet. Please try in a later version of the game')

        else:
            print()
            type_effect('invalid input.')
    
    except:
        pass