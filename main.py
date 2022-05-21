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

def start_stats(): #health - money - inventory  ALL = 0
    health = 100
    money = 0

def game_begin(): #starts the game - probably not needed
    loading("start")
    start_stats()
    introduction()

if __name__ != 'main':
    game_begin()
    print()
    ok=input('STILL TESTING. GAME END')