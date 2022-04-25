#think of this file as a test bed of sorts

import sys
from time import sleep
from main import *
from object import Object

#name, player_room, description = 'void', room = 'void', takeable = False, inInventory = False, health = 0, money = 0, code = 000
x = Object('key', 'start', 'start', 'void', True, False)

#x.add_description("this is a large grey key. It sucks!")

x.item_description('void','void')

#x.test()