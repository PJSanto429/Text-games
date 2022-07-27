from typeEffect import type_effect
from object import *
from room import *
from saveGame import *
from gameBegin import gameHelpMain

#constants:
cantSee = "Hmm, I can't see that"
noDesc = "I see nothing special about that"

thing = Object('void', 'none')
room = Room()

def text_input(text, player_room, version = 'main'):
    text = text.lower()
    fullText = text
    text = text.split()
    try:
        action = text[0]
        x = len(text)

        if action in ['quit', 'exit', 'stop']:
            quit_save(player_room, version)

        elif len(text) == 1 and action in ['inv', 'inventory']:
            thing.see_inventory()
            
        elif fullText == 'look at me':
            #this stuff will be stored in room class until player class is built
            room.player_look()

        elif action == 'wait':
            print()
            type_effect('Time passes...')
        
        elif action in ['items', 'objects']:
            room.get_room_items(player_room)
            
        elif len(text) == 1:
            if action in ['l', 'look']:
                room.action('look', player_room)

            elif action == 'drop':
                thing.drop_input_sorter(player_room)

            elif action == 'take':
                thing.take_input_sorter(player_room)

        elif action in ['move', 'go']:
            room.action('move', player_room, text[x - 1])
        
        elif action == 'save':
            saveGame(player_room, version)

        elif action == 'load':
            player_room = loadGame(version)
            room.go(player_room)
            room.action('look', player_room)

        elif action in ['drop', 'take', 'look', 'l', 'examine'] or (action in Object.otherActions):
            if version in  ['dev', 'main']:
                thing.action_input_sorter(action, player_room, text, fullText)

        elif action == 'put':
            if version in ['dev', 'main']:
                thing.put_into_input_sorter(fullText, player_room)

        elif action in ['help()', 'help']:
            if version in ['dev']:
                gameHelpMain()
            if version in ['main']:
                print()
                type_effect('Sorry, but this function is not available yet. Please try in a later version of the game')

        else:
            print()
            type_effect('invalid input.')
    
    except:
        pass