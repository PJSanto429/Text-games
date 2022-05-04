#think of this file as a test bed of sorts

import sys
from time import sleep
from gc import get_objects
from main import *
from object import Object, player_inventory
from room import Room

#text_input('look at key', 'start')

#Here is a color
'''
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
print(colored(0, 255, 0, 'Hello, World'))'''

key.return_name()

'''while True:
    print()
    text = input("Input: ")
    text_input(text)'''

'''import weakref

class A:
    instances = []
    def __init__(self, name=None):
        self.__class__.instances.append(weakref.proxy(self))
        self.name = name

a1 = A('a1')
a2 = A('a2')
a3 = A('a3')
a4 = A('a4')

for instance in A.instances:
    print(instance.name)'''