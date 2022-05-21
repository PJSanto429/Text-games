#text input

from typeEffect import type_effect
from object import Object
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
    text = text.split()
    action = text[0]
    x = len(text)

    if text[0] == 'quit' or text[0] == 'quit()' or text[0] == 'stop':
        print()
        type_effect('Quitting...')
        quit()

    elif action == 'testing' or action =='inv' or action == 'inventory':
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
    
    elif len(text) == 1 and action == 'look' :
        room.action('look', player_room)

    elif action == 'move' or action == 'go':
        room.action('move', player_room, text[x - 1])
    
    elif action == 'take' or action == 'drop' or action == 'look':
        thing.action(action, text[x - 1], player_room)

    elif action == 'save':
        saveGame(player_room)

    elif action == 'load':
        inventory, room1 = loadGame()
        for i in Object.instances:
            if i.longName in inventory:
                i.inInventory = True
        player.room = room1
