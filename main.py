#This 'game' is less of a game and more of a pet project type thing. it is nowhere close to being done it is just fun to work on

'''Last edited: 4/30/22 @ 10:46 PM ==> Last worked on:
In order of newest to oldest:

=> worked on object class some more
    => in testBed.py there is a useable 'live' simulation for looking, taking and dropping items.

=>fixed look at and take and drop. DO NOT IMPORT FROM TESTBED. IDK why, but it will print stuff twice. very annoying

=> Worked on Object class a little more. => change name, description, isTakeable, item description should work(add descriptions)
    => rearanged objectpropertie to what will be best (less used stuff with be at the end and vice versa)
=> Changed typeWrite.py to testBed.py (makes more sense to have new name)
'''

#To-Do list(In order of most to least importance):
'''
            1. Work on Object class  ###MOST IMPORTANT: Game will mostly not function without this
                A. picking up and dropping stuff
                    I. Inventory system: still pretty bare bones and incomplete
                        1. add stuff to player_inventory while taking it from room inventory and vice versa
                    II. Make sure that item is in player room
                        1. maybe check if the item room and player room are the same as a first step?

                B. Item Descriptions
                    I. For stuff with no description, put: "I see nothing special about (item)"
                    II. For stuff not in room, put: "Hmm, I can't see that'

            2. Work on Room class #Most recent addidion => not good yet
                A. room descriptions
                B. room inventories
                C. to make a room, make a def that creates the room and all the fun stuff, and then tell ths player what to do, etc.

            3. Text Input  ###VERY IMPORTANT: should be 1, but I don't want to work on it because it is quite boring. Also it will be much easier to do once previous stuff is done
                A. get it working. it pretty much does nothing
                B. When more complete, integrate with Object class(item descriptions, inventory, etc)

                    stuff up here is the bones and meat of the project, CAN  be transfered to another game.
---------------------------------------------------------------------------------------------------------------
                    stuff down here is more specific to the game, this is the creative part
                    (#4 - player movement is pretty simple to change for another game)
                    (#5 - stuff to do is the most creative part and would change most for a new project)

            4. Player movement(room to room)   ##Pretty Important: not nearly as important as 1, but still vital to making the game work. game won't work at all past the starting room without this
                A. maybe add different 'look' directions 
            
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
                '''

#imports
from time import sleep
import sys
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from random import randint, choice
from object import Object, player_inventory
from room import Room

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

'''these items are just for testing purposes'''
#name, room = 'void', description = 'void', takeable = False, inInventory = False, health = 0, money = 0, longName = 'void', code = 000
key = Object('key', 'void', 'this is a large gold key', True, False, 'large gold key')
key2 = Object('key', 'void', 'this is a small bronze key', True, False, 'small bronze key')

cat = Object('cat', 'void', 'this is a big grey cat, with very long whiskers', False, False, 'big grey cat')
cat2 = Object('cat', 'void', 'this is a small black cat, with very well kept fur', False, False, 'small black cat')

chair = Object('chair', 'void', 'this is a large fancy chair whith large butt marks', False, False, 'large chair')
chair.notTakeable_message('this chair is bolted to the floor, making it unable to be moved')

'''most of the items in the '2' rooms are for testing and demonstrations'''
#starting room stuff:
note = Object('note', 'start', 'this is a standard sheet of paper, with a bunch of words witten on it. Might be worth a shot to read it', True, False, 'standard note')
note.add_attribute('read', "This is a note! I can't believe that I wrote a note and you are actually reading it! Woohoo!")

chair2 = Object('chair', 'start', 'this is a rusted folding chair that looks like it has been welded to the floor', False, False, 'rusty folding chair')

#stuff in room 2:
chair3 = Object('chair', 'room2', 'this is a cool looking dining room chair', False, False, 'dining room chair')

def text_input(text, player_room='none'): #not done (getting there)text = text.lower()
    text = text.split()
    action = text[0]
    x = len(text)

    if text[0] == 'quit' or text[0] == 'quit()':
        print()
        type_effect('Quitting...')
        quit()

    if action == 'testing':
        print()
        #type_effect('testing')
        type_effect('Your inventory consists of:')
        if len(player_inventory) > 0:
            for thing in player_inventory:
                print()
                type_effect(thing)
        else:
            print()
            type_effect('Nothing yet...')

    elif text[x - 1] == 'key':
        key.action(action, player_room)
    elif text[x - 1] == 'cat':
        cat.action(action, player_room)
    elif text[x - 1] == 'chair':
        chair.action(action, player_room)
    elif text[x - 1] == 'note':
        note.action(action, player_room)
    elif text[x - 1] == 'wall':
        try:
            wall.action(action, player_room)
        except:
            pass

    else:
        print()
        type_effect("something went wrong")

'''def inventory(player_room, action='look'): #NOT DONE | work on this second - OR NEVER...
    if player_room == "starting_room":
        room_inv = starting_room_INV
    elif player_room == 'room_one':
        room_inv = RM_1_INV
    else:
        ok=input('error')
        quit()
    
    if action == 'look': #pretty good, maybe done
        for thing in room_inv:
            print()
            type_effect(thing)
    
    elif action == 'take': #add 
        print('TAKE')

    elif action == 'drop':
        print('DROP')'''

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
    starting_room()

def starting_room(): #nothing here yet...
    print()
    type_effect('This is a super cool room.')

if __name__ != 'main':
    game_begin()
    print()
    ok=input('STILL TESTING. GAME END')