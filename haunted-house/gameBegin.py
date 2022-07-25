from object import *
from typeEffect import type_effect
from textInput import *

thing2 = Object()
    
def gameHelpMain():
    seen = False
    options = ['inventory', 'item interaction', 'save/load']
    while True:
        print()
        if not seen:
            seen = True
            type_effect('Welcome to the help function. Please type what you need help with. Your options are: ')
            for option in options:
                print()
                type_effect(option)
        else:
            type_effect('please make another choice, or type DONE to resume the game')
        print()
        choice = input('choice: ').lower()
        if choice in options:
            if choice == 'inventory':
                gameHelpInventory()
            if choice == 'item interaction':
                itemInteractionHelp()
            if choice == 'save/load':
                saveLoadHelp()
        elif choice == 'done':
            break
        else:
            print()
            type_effect('invalid input.')
        
def saveLoadHelp():
    print()
    type_effect('-------------- Saving/Loading -----------------------', 'white')
    print()
    type_effect('saving and loading is very helpful when you would like to take a break from the game and resume at a later time')
    print()
    print('--------------------------------------')
    type_effect('to save a game , simply type \'save\'')
    print()
    type_effect('when saving a game, you can either create a new save file or save to an existing file')
    print()
    type_effect('if you wish to create a new file, you will be promted for a name and password(password not reqired, only needed for protecting save file)')
    print()
    type_effect('if you wish to save to an existing file, the same thing will happen only the new save file will overwrite an existing one')
    print()
    print('--------------------------------------')
    type_effect('to load a game, simply type \'load\'')
    print()
    type_effect('you will then be asked for your save code(given to you when you create a save file) and the save password(if neccessary)')
    print()
    type_effect('the game will then load everything to the way it was when you saved it')

def itemInteractionHelp():
    print()
    type_effect('-------------- Item Interaction -----------------------', 'white')
    print()
    print()
    type_effect('interacting with items is a large part of this game. here are a few things to remember:')
    print()
    type_effect('to interact with items, type the action you would like to do, followed by the item name. ex:')
    print()
    type_effect('look at key, take standard note, etc')
    print()
    type_effect('if you type the items full name(rusty copper key, clean fridge), you will simply get the item description or action, like so:')
    print()
    type_effect('this is a large marble statue, with several chunks missing. i wonder how old it might be...')
    print()
    print('---------------------------------------')
    type_effect('if you type the items short name(key, fridge), you might get a prompt to be more specific. the prompt will look like this:')
    print()
    type_effect('which did you mean?')
    print()
    type_effect('rusty copper key')
    print()
    type_effect('fancy jade key')
    print()
    type_effect('you would then type the full name of the item you meant.')
    print()
    print('---------------------------------------')
    print()
    type_effect('here are the standard action you will be able to do(there are other actions, but these are the most common ones):')
    print()
    print('---------------------------------------')
    type_effect('------------ \'Look At\' items ------------')
    print()
    type_effect('to look at an item, you type: look at (item name)')
    print()
    type_effect('eg. look at rusty copper key')
    print()
    print('---------------------------------------')
    type_effect('------------ \'Take/Drop\' items ------------')
    print()
    type_effect('to take or drop an item, you type: take/drop (item name)')
    print()
    type_effect('eg. take hat, drop tennis ball')
    print()
    type_effect('')
    print()
    print('---------------------------------------')
    type_effect('------------ \'Open/Close\' container ------------')
    print()
    type_effect('to open or close a container, type: open/close (container name)')
    print()
    type_effect('eg. open box, close large gold chest')
    print()
    type_effect('if a container is locked, you will be prompted to unlock it. the prompt will look like:')
    print()
    type_effect('large gold chest is locked. would you like to try and unlock it?')
    print()
    print('---------------------------------------')
    type_effect('------------ \'Lock/Unlock\' container ------------')
    print()
    type_effect('to lock or unlock a container, type: lock/unlock (container name)')
    print()
    type_effect('eg. lock box, unlock large gold chest')
    print()
    print('---------------------------------------')
    type_effect('------------ \'Put Into\' container ------------')
    print()
    type_effect('to put an item into a container, type: put (item) into (container)')
    print()
    type_effect('eg. put rusty copper key into chest, put note into large metal box')
    print()
    print('---------------------------------------')
    type_effect('------------ \'other action\' container/item ------------')
    print()
    type_effect('there are other actions you can do, like read, eat, drink, etc. to do these, type: other action (item)')
    print()
    type_effect('eg. read note, drink bottle, eat hamburger')

def gameHelpInventory():
    print()
    type_effect('------------------------- INVENTORY -------------------------', 'white')
    print()
    type_effect("To view your inventory, type 'inv' or 'inventory'")
    print()
    type_effect('this will get you something like this:')
    print()
    thing2.see_inventory(True)
    
#--------------------------------------------------------------------
#tutorial
def tutorial():
    itemInteractionHelp()
    print()
    saveLoadHelp()
    print()
    gameHelpInventory()
    print()
    type_effect("This concludes the tutorial, please press ENTER to start the game")
    choice = input()

#introduction
def introduction(): #pretty much done
    print()
    type_effect("If you need to see a tutorial on the game mechanics, please type 1 now. Otherwise, please type 2. ")
    choice = input()
    if choice == '1':
        tutorial()
    print()
    type_effect('welcome to the game engine. there will hopefully be ')