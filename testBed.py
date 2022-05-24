#think of this file as a test bed of sorts
import sys
from time import sleep
from gc import get_objects
from main import *
from object import Object, player_inventory
from room import Room, player
from saveGame import *
from loading import loading
from typeEffect import *
from datetime import datetime

x = 1
match x:
    case 1:
        print('hello')

'''
player.room = 'first'
text_input('look', player.room)
while True: #this is a very simple interactive 'window' that allows for text input
    print()
    text = input("Input: ")
    text_input(text, player.room)'''