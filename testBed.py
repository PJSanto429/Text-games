#think of this file as a test bed of sorts

import sys
from time import sleep
from main import *
from object import Object, player_inventory
from room import Room

while True:
    print()
    text = input("Input: ")
    text_input(text)