#imports---------------------
#python built in imports
from time import sleep, time
import sys
import json
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from random import randint, choice

# my imports - files I made
from object import *
from room import *
from items import *
from loading import *
from typeEffect import *
from textInput import *
from textColor import *
from gameBegin import *
from firstStartup import *

if __name__ == '__main__':
    #start_stats() #might not be needed

    #introduction() #needs to be changed
    print('---------------------main build-(v 0.2.0)--------------------')
    firstStartup()
    loading("start")
    player.room = 'first'
    text_input('look', player.room)
    
    while True: #live version of the game in version main
        print()
        text = input(">> ")
        text_input(text, player.room)