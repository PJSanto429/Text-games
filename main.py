#This 'game' is less of a game and more of a pet project type thing. it is nowhere close to being done it is just fun to work on
'''Last edited: 4/22/22 @ 10:45 PM'''
'''To-Do list(In order of most to least importance):

            1. Work on Object class  ###MOST IMPORTANT: Game will mostly not function without this
                A. picking up and dropping stuff
                    I. Inventory system: still pretty bare bones and incomplete
                B. Item Descriptions
                    I. For stuff with no description, put: "I see nothing special about (item)"
                    II. For stuff not in room, put: "Hmm, I can't see that'

            2. Player movement(room to room)   ##Pretty Important: not nearly as important as 1, but still vital to making the game work. game won't work at all past the starting room without this
                A. maybe add different 'look' directions 

            3. Text Input  ###VERY IMPORTANT: should be 1, but I don't want to work on it because it is quite boring
                A. get it working. it pretty much does nothing
                B. When more complete, integrate with Object class(item descriptions, inventory, etc)

            4. Stuff to do/get
                A. Find treasure/trophies
                B. Solve puzzles
                C. Other characters
                    I. Enemies
                    II. Friendlies
                        1. Companians such as a dog or hobbit-type thing(idk if hobbits are nice but in this game they will be)
                    III. Shopkeepers/merchants
                '''

#imports
from time import sleep
import sys
from random import randint

#constants:
yes = ['yes','y'] #these two are for asking the player simple questions: if choice in yes:
no = ['no','n']

def type_effect(text): #typewriter effect. idk how it works
    words = text
    for char in words:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

def start_stats(): #health - money - inventory  ALL = 0
    health = 100
    money = 0
    inventory = []

#room inventories:
void = []
starting_room_INV = ['house','chair','cat'] #these are not going to end up in the 'final' product, currently being used for testing 
RM_1_INV = []

item_list = starting_room_INV + RM_1_INV

'''
#all items:
def item_descriptions(item): #Add descriptions for ALL items
    #if item in player_room  #make sure that the item getting looked at is in the room the player is in
    if item == 'key':
        print()
        type_effect("This is a large gold key, with a large amount of rust all over the handle")
    if item == 'cat':
        print()
        type_effect("this is a very cool looking cat")
        '''


def text_input(text, player_room): #not done (not even close) work on this first
    text = text.lower()
    text = text.split()
    if text[0] == 'look':
        if text[1] == 'at':
            if text[2] in item_list:
                pass
                #item_description(text[2])
    
    if text[0] == 'take':
        pass            #find a way to make sure that the item is able to be taken(in the players current room)

def inventory(player_room, action='look'): #NOT DONE | work on this second
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
        print('DROP')

error_message = 'Oops! It seems that something went wrong with what you typed. You will be redirected to make your last decision again.'

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
    type_effect("(You Type) Pick up Knife")
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
    #inventory(starting_room)
    global player_room
    player_room = 'start'
    print()
    type_effect("You are in small, dark room, with beautiful ")

if __name__ != 'main':
    game_begin()
    print()
    ok=input('STILL TESTING. GAME END')