#tutorial and introduction

from typeEffect import type_effect
from time import sleep
from textInput import *
from loading import error_message

'''PRETTY MUCH EVERYTHING IN THIS FILE IS GARBAGE.
    It was the first stuff that i worked on(before the actual engine) and is therefore obsolete
    It will need to be changed if this ever turns into a real game, but it is fine for now
        - none of it is being used, so who cares
        - the introduction will need to be changed the most because it is the only 'story' this has
        - the tutorial will pretty much stay the same, just a few thing will change:
            + how the actual mechanics of the game are supposed to be used
        - start_stats will eventually be be integrated once there are items that:
            + have value(positive or negative)
            + have health(whether it heals or hurts the user)'''

#start stats
def start_stats(): #health - money  ALL = 0
    health = 100 #probably not needed yet
    money = 0
    
def gameHelpMain():
    options = ['inventory', 'item interaction', 'save/load']
    print()
    type_effect('Welcome to the help function. Please type what you need help with. Your options are: ')
    print()
    for option in options:
        print()
        type_effect(option)
    choice = input('choice: ').lower()
    if choice in options:
        pass
    else:
        print()
        type_effect('invalid input.')

def gameHelpInventory():
    print('------------------------- INVENTORY HELP -------------------------')
    type_effect("To view your inventory, type 'i', 'inv', or 'inventory'")
    print()
    type_effect('this will get you something like this:')
    print()
    type_effect('your inventory consists of:')

#tutorial
def tutorial(): #done
    type_effect("In this game, you will be presented with information including the room you are in. The room information will look like this:")
    print()
    print()
    type_effect("You are in a dark, musty library with faded red carpets and peeling wallpaper. It seems that no one has been here in quite some time, as every surface is covered with dust. There is a great big window on the North wall, but the curtains are closed so you cannot see outside...")
    print()
    print()
    type_effect("You are able to look at things that might seem interesting. To do so, type something like this:")
    sleep(.5)
    print()
    print("Look at wallpaper")
    print()
    type_effect("This will tell you something like this:")
    print()
    type_effect("The wallpaper is peeling and very faded, but it seems that it was never good looking. It seems that it was a terrible shade of yellow when it was fresh.")
    print()
    print()
    type_effect("To move from room to room, you will be told which directions you are able to go (North, South, East, or West). Moving information will look like this:")
    print()
    type_effect("You can go SOUTH or WEST")
    print()
    type_effect("You then type which direction you would like to go, like this:")
    print()
    print()
    type_effect("(You Type) Go South")
    print()
    print()
    type_effect("While walking around, there will be some stuff you will be able to pick up(and drop as well). The pickup/drop/inventory system will go like this: ")
    print()
    print()
    type_effect("You can see a Book, a Key, and a Knife")
    print()
    sleep(.5)
    print()
    type_effect("(You Type) Take Knife")
    print()
    sleep(.5)
    type_effect("You have picked up the Knife!")
    print()
    sleep(.5)
    print()
    type_effect("(You Type) Drop Knife")
    print()
    sleep(.5)
    type_effect("You have dropped the Knife!")
    print()
    sleep(.5)
    print()
    type_effect("(You Type) View inventory")
    print()
    sleep(.5)
    type_effect("Your inventory consists of:")
    print()
    type_effect("Map")
    print()
    type_effect("Flashlight")
    print()
    type_effect("Rose")
    #print()
    #print()
    #type_effect("There are a various amount of things that you can do with items in your inventory, such as Throw, kick, Use, etc.")
    print()
    print()
    type_effect("In this game, spelling is very important, as a mistake will lead to an error message like this:")
    print()
    type_effect(error_message)
    print()
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
    else:
        pass
    print()
    type_effect("Welcome to HAUNTED HOUSE: TRANSYLVANIA. In this game, you will be walking around a haunted house in - you guessed it - Transylvania. ")
    print()
    type_effect("While walking around, you are likely to encounter some of Translyvania's residents(warewolves, zombies, mummies, and Dracula himself.).")
    print()
    type_effect("Some of these guys are going to try and kill you, while the others are looking to eat you. This means that there is no one to trust, except maybe the ghost.")
    print()
    type_effect("You will have to find some clues, solve different puzzles, try to survive, and most importantly, escape.")
    print()
    type_effect("I am your narrator, NEODAR. If you need me help at any point, just type help() and I will 'help' you.")
    print()
    type_effect("There are a lot of other things that you probably need to know before the game starts, but I'm not gonna tell you. You'll figure it out at some point. I hope.")
