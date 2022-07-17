#text input

from typeEffect import type_effect
from object import *
from room import *
from saveGame import *

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

        elif action in ['inv', 'inventory']:
            thing.see_inventory()
        
        elif action in ['items']:
            room.get_room_items(player_room)
        
        elif action == 'items':
            pass

        elif action == 'wait':
            print()
            type_effect('Time passes...')
        
        elif len(text) == 1 and (action in ['l', 'look']):
            room.action('look', player_room)

        elif action in ['move', 'go']:
            room.action('move', player_room, text[x - 1])
        
        elif action == 'save':
            saveGame(player_room, version)

        elif action == 'load':
            player_room = loadGame(version)
            room.go(player_room)
            room.action('look', player_room)

        elif action == 'take' or action == 'drop' or (action == 'look' or action == 'l' ) or (action in Object.otherActions):
            #move all of this into object.py to clean it all up
            x = 0
            if version in ['main', 'dev']:
                actions = ['take ', 'pick ', ' up ', 'drop ', 'look ', 'at ']
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
                    thing.action(action, text[x - 1], player_room)

        elif action == 'put': # this needs to be worked on => it needs to be put into a function in object.py to clean this file up
            if version == 'dev':
                fullText = fullText.replace('put ', '')
                text = fullText.split('into')
                text[0], text[1] = text[0].strip(), text[1].strip()
                for i in Object.instances:
                    if text[0] == i.longName:
                        i.put_into_container(text[1])
                            
            if version == 'main':
                print()
                type_effect('invalid input.')

        elif action == 'help()':
            if version == 'dev':
                print()
                type_effect('function needs to be added => check the section above #2 in todo.py')
            if version == 'main':
                print()
                type_effect('Sorry, but this function is not available yet. Please try in a later version of the game')

        else:
            print()
            type_effect('invalid input.')
    
    except:
        pass