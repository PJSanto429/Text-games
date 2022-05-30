#To-Do list(In order of most to least importance):
'''        4. Work on save/load system more
                A. add all items and the room that they are in
                    I. this will most likely get more complicated when there are puzzles that need to stay solved during save states
                B. when multiple save states are loaded, some items are lost
                    I. add a self.homeRoom to objects
                    II. move all objects back to home room and then load

                C. add a time to each save file
                    I. when quitting, check all save files => if too much time has passed between last save, ask if player would like to save before quitting

                D. maybe add auto-save(more for player convenience)

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
                    IV. use faker to create fake names for these characters
                        1. Documentation: https://faker.readthedocs.io/en/master/
            
            6. Add graphics? --last thing to do
                A. use pygame
                    I. https://www.101computing.net/getting-started-with-pygame/'''

#imports---------------------
#python built in imports
from time import sleep
import sys
import json
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from random import randint, choice

# my imports - files I made
from object import Object, player_inventory
from room import Room
from items import *
from loading import loading
from typeEffect import *
from textInput import *
from textColor import *
from gameBegin import *
from firstStartup import *

def start_stats(): #health - money  ALL = 0
    health = 100
    money = 0

def game_begin(): #starts the game - probably not needed
    loading("start")
    start_stats()
    introduction()
    player.room = 'first'
    text_input('look', player.room)
    while True:
        print()
        text = input("Input: ")
        text_input(text, player.room)

try:
    startup()
except:
    pass

if __name__ == '__main__':
    #game_begin()
    #start_stats()
    loading("start")
    start_stats()
    introduction()
    player.room = 'first'
    text_input('look', player.room)
    while True:
        print()
        text = input("Input: ")
        text_input(text, player.room)