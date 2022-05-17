from object import Object
from room import Room

'''these items are just for testing purposes'''
#name, room = 'void', description = 'void', takeable = False, inInventory = False, health = 0, money = 0, longName = 'void', code = 000
key1 = Object('key', 'void', 'this is a large gold key', True, False, 'large gold key')
key2 = Object('key', 'void', 'this is a small bronze key', True, False, 'small bronze key')

cat1 = Object('cat', 'void', 'this is a big grey cat, with very long whiskers', False, False, 'big grey cat')
cat1.notTakeable_message('As you are trying to pick up the big grey cat, it keeps jumping out of your arms. This may not be the best idea')

cat2 = Object('cat', 'void', 'this is a small black cat, with very well kept fur', False, False, 'small black cat')
cat2.notTakeable_message('As you are trying to pick up the small black, it keeps jumping out of your arms. This may not be the best idea')

chair1 = Object('chair', 'void', 'this is a large fancy chair whith large butt marks', False, False, 'large chair')
chair1.notTakeable_message('this chair is bolted to the floor, making it unable to be moved')

wall = Object('wall', 'void', 'this is a wall', False, False, 'boring grey wall')

#===================================================================

#-----------------------ROOM ONE ----------- Room creation
room1 = Room('first')
room1.set_directions(False, 'second', False, False)
room1.change_description('You are in a dark, musty kitchen')

#room items ______________________
note1 = Object('note', 'first', 'this is a standard sheet of paper, with a bunch of words witten on it. Might be worth a shot to read it', True, False, 'standard note')
note1.add_attribute('read', "This is a note! I can't believe that I wrote a note and you are actually reading it! Woohoo!")

key3 = Object('key', 'first', 'this is a rusty copper key', True, False, 'rusty copper key')

chair2 = Object('chair', 'first', 'this is a rusted folding chair that looks like it has been welded to the floor', False, False, 'rusty folding chair')

#===================================================================
#----------------------- ROOM TWO ----------- Room creation
room2 = Room('second')
room2.change_description('You are in test room')
room2.set_directions('first', False, False, 'third')

#room items ______________________
key4 = Object('key', 'second', 'this is a normal house key, with all the accommodating notches', True, False, 'normal house key')

hat1 = Object('hat', 'second', 'this is a sun hat', True, False, 'sun hat')

#===================================================================
#----------------------- ROOM THREE ----------- Room creation 
room3 = Room('third')
room3.set_directions(False, False, 'second', False)
room3.change_description('this is the third room, another test room')

#room items ______________________
bottle1 = Object('bottle', 'third', 'this is an empty beer bottle', True, False, 'empty beer bottle')