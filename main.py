#To-Do list(In order of most to least importance):
'''        
            5. Stuff to do/get    #fun stuff(for player), wrap up
                A. Find treasure/trophies
                B. Solve puzzles
                C. Other characters
                    I. Enemies
                    II. Friendlies
                        1. Companion such as a dog or hobbit-type thing(idk if hobbits are nice but in this game they might be)
                        2. characters that help you occasionally
                    III. Shopkeepers/merchants
                        1. Buy stuff - set object money to negative initially, then set it to zero after taking it
                    IV. use faker to create fake names for these character
                        1. Documentation: https://faker.readthedocs.io/en/master/
            
            6. Add graphics? --last thing to do
                A. use pygame
                    I. https://www.101computing.net/getting-started-with-pygame/'''

#imports
from time import sleep
import sys
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from random import randint, choice
from object import Object, player_inventory
from room import Room
from items import *
import json

#constants:
yes = ['yes','y'] #these two are for asking the player simple questions: if choice in yes:
no = ['no','n']
cantSee = "Hmm, I can't see that"
noDesc = "I see nothing special about that"
error_message = 'Oops! It seems that something went wrong with what you typed. You will be redirected to make your last decision again.'

class color: #this allows text to be colored
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def type_effect(text = ""): #typewriter effect. idk how it works
    words = text
    for char in words:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

def rand_let(amount=1, choice='all'):  #TOTAL GARBAGE. error = 'str' object is not callable. IDK what to do and I don't really care
    randLetList = []
    a = (ascii_letters)
    '''if choice == 'all':
        x = ascii_letters
    elif choice == 'upper':
        x = ascii_uppercase
    elif choice == 'lower':
        x = ascii_lowercase'''

    for i in range(amount):
        y = randint(1,100)
        randLetList.append(y)

    type_effect(randLetList)
    #random.choice(string.ascii_letters)

def start_stats(): #health - money - inventory  ALL = 0
    health = 100
    money = 0

#---------------------THESE ARE HERE SO THE CODE CAN LOOK INTO ALL ROOM/OBJECT INSTANCES
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
        pass

    elif action == 'load':
        pass

def loading(message): #done
    if message == 'restart':
        message1 = 'SYSTEM RESTARTING... PLEASE STAND BY'
        message2 = 'REBOOT SUCCESSFUL'
        
    elif message == 'start':
        message1 = 'SYSTEM STARTING... PLEASE STAND BY'
        message2 = 'GAME BOOT SUCCESSFUL'

    elif message == 'quit':
        message1 = 'SYSTEM ENDING... PLEASE STAND BY'
        message2 = 'SYSTEM QUIT SUCCESSFUL'

    else:
        print('error')
        quit()

    print()
    type_effect(message1)
    sleep(2)
    print()
    type_effect('0%__________10%__________20%__________30%__________40%__________50%__________60%__________70%__________80%__________90__________100%')
    print()
    sleep(2)
    type_effect(message2)
    sleep(2)
    print()

def error(): #done
    print()
    type_effect(error_message)
    sleep(2)

def ask_quit(): #done
    print()
    type_effect('Are you sure that you would like to quit? You will lose all progress. ')
    choice = input()
    choice = choice.lower()
    if choice in yes:
        print()
        loading('quit')
        quit()
    else:
        print()
        type_effect('Good choice. You will be redirected to make your last decision again')

def ask_restart(): #done
    print()
    type_effect('Are you sure that you would like to restart? You will lose all progress and be redirected back to the beginning of the game. ')
    choice=input()
    choice=choice.lower()
    if choice in yes:
        loading('restart')
        game_begin()
    else:
        print()
        type_effect("If you did not want to restart, why did you type it? GAME CONTINUING... PLEASE STAND BY")

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
    print()
    print()
    type_effect("There are a various amount of things that you can do with items in your inventory, such as Throw, kick, Use, etc.")
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

#rooms
def game_begin(): #starts the game, DONE
    loading("start")
    start_stats()
    introduction()

def starting_room1():
    while True:
        print()
        print()
        text = input(">> ")
        text_input(text, 'start')

if __name__ != 'main':
    game_begin()
    print()
    ok=input('STILL TESTING. GAME END')