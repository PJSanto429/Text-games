#think of this file as a test bed of sorts
import sys
from time import sleep
from gc import get_objects
from main import *
from object import Object, player_inventory
from room import Room, player

player.room = 'first'
text_input('look', player.room)
while True: #this is a very simple interactive 'window' that allows for text input
    print()
    print()
    text = input("Input: ")
    text_input(text, player.room)