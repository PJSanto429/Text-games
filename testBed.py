#think of this file as a test bed of sorts

import sys
from time import sleep
from gc import get_objects
from main import *
from object import Object, player_inventory
from room import Room

'''from colorama import init
from termcolor import colored

init()
print(colored('Hello World', 'black', 'on_white'))'''

#type_effect(color.YELLOW + 'this is super cool') #this is a pretty cool class/function that adds color to text

#text_input('look at cat')

#text_input('look at cat')

#print("This is bold text looks like:",'\033[1m' + 'Python' + '\033[0m')

#print(key.return_name('longname'))

#key.test('keyList')

while True: #this is a very simple interactive 'window' that allows for text input
    print()
    text = input("Input: ")
    text_input(text)