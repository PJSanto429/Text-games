# despite the name of this file, there is no typewriting being done
#think of this file as a test bed of sorts

import sys
from time import sleep
from main import *
from object import Object

#name, player_room, description = 'void', room = 'void', takeable = False, inInventory = False, health = 0, money = 0, code = 000
x = Object('key', 'start', 'start', 'This is a large skeleton key, with a lot of rust all over the handle', True, False)

x.test()