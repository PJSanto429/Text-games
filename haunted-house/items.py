from object import Object
from room import Room

'''these items are just for testing purposes'''

key1 = Object('key', 'void', 'this is a large gold key', True, False, 'large gold key')
key2 = Object('key', 'void', 'this is a small bronze key', True, False, 'small bronze key')
key2.add_aliases(['bronze key', 'small key']) #has to be a list

cat1 = Object('cat', 'void', 'this is a big grey cat, with very long whiskers', False, False, 'big grey cat')
cat1.notTakeable_message('As you are trying to pick up the big grey cat, it keeps jumping out of your arms. This may not be the best idea')

cat2 = Object('cat', 'void', 'this is a small black cat, with very well kept fur', False, False, 'small black cat')
cat2.notTakeable_message('As you are trying to pick up the small black cat, it keeps jumping out of your arms. This may not be the best idea')

chair1 = Object('chair', 'void', 'this is a large fancy chair whith large butt marks', False, False, 'large chair')
chair1.notTakeable_message('this chair is bolted to the floor, making it unable to be moved')

#-----------------------ROOM ONE ----------- Room creation
room1 = Room('first')
room1.set_directions(False, 'second', False, False)
room1.change_description('You are in a dark, musty kitchen with peeling wallpaper and a gross looking fridge. there is really nothing else in here')

#room items ______________________
fridge1 = Object('fridge', 'first', 'this is a very old, very large, and very gross fridge. the smell coming off of it makes you wonder what could possibly be in it', False, False, 'gross fridge')
fridge1.open_description('this is a great big stinky fridge with a broken light, so it is hard to see what it inside')
fridge1.add_attribute('open', 'with some effort, you are able to open the fridge. there is really nothing special about it when it is open.', 'open')
fridge1.add_attribute('close', 'you shut the fridge, hoping to get rid of some of the awful smell, but no luck', 'close')
fridge1.add_attribute('smell', 'Yuck!')
fridge1.create_container(True, 'rusty copper key', True)

fridge2 = Object('fridge', 'first', 'this is a clean fridge that looks brand new', False, False, 'clean fridge')
fridge2.open_description('the inside of this fridge is somehow even cleaner than the outside')
fridge2.add_attribute('open', 'this fridge opens with no effort', 'open')
fridge2.add_attribute('close', 'this fridge closes very nicely and it practically silent', 'close')
fridge2.create_container(False)

ketchup1 = Object('ketchup', 'first', 'this is a bottle of ketchup', True, False, 'ketchup bottle', 'gross fridge')
ketchup2 = Object('ketchup', 'first', 'this is an empty bottle of ketchup', True, False, 'empty ketchup bottle')

mustard1 = Object('mustard', 'first', 'this is a bottle of mustard', True, False, 'mustard bottle', 'gross fridge')

wallpaper1 = Object('wallpaper', 'first', 'void', False, False, 'peeling wallpaper')

note1 = Object('note', 'first', 'this is a standard sheet of paper, with a bunch of words witten on it. Might be worth a shot to read it', True, False, 'standard note')
note1.add_attribute('read', "the note reads: This is a note! I can't believe that I wrote a note and you are actually reading it! Woohoo!")

key3 = Object('key', 'first', 'this is a rusty copper key. parts of it are turning green, so it is pretty old', True, True, 'rusty copper key')
key3.add_aliases(['copper key', 'rusty key'])

key4 = Object('key', 'first', 'this is a bent car key. it is hard to tell what type of car it went with, but it obviously would not work in its current condition', True, True, 'bent car key')
key4.add_aliases(['car key', 'bent key'])

key5 = Object('key', 'first', 'this is a fancy jade key, with a very shiny handle. i wonder what it might unlock?', True, False, 'fancy jade key')

chair2 = Object('chair', 'first', 'this is a rusted folding chair that looks like it has been welded to the floor. why would someone do that?', False, False, 'rusty folding chair')

chair3 = Object('chair', 'first', 'this is a very comfortable looking aderondac chair. adirondach. adorondack. adirondack. did i spell that right?', False, False, 'adirondack chair')

cat3 = Object('cat', 'first', 'this is a fat tabby cat, with very long fur', False, False, 'fat tabby cat')
cat3.notTakeable_message('As you are trying to pick up the fat tabby cat it keeps jumping out of your arms. This may not be the best idea')
cat3.add_aliases(['fat cat', 'tabby cat'])

#===================================================================
#----------------------- ROOM TWO ----------- Room creation
room2 = Room('second')
room2.change_description('You are in an oddly shaped room, with weird ovals everywhere. nothing makes any sense, except for the fact that nothing makes sense')
room2.set_directions('first', False, False, 'third')

#room items ______________________
key4 = Object('key', 'second', "this is a normal house key, with all the accommodating notches. the number on the key is 549, but i'm not sure how important that is", True, False, 'normal house key')

hat1 = Object('hat', 'second', 'this is a sun hat, like the ones old women wear to the beach', True, False, 'sun hat')
hat1.add_attribute('wear', 'you put the sun hat on, but take it off after you realize that it relly isnt your style.')

#===================================================================
#----------------------- ROOM THREE ----------- Room creation 
room3 = Room('third')
room3.set_directions(False, False, 'second', False)
room3.change_description('you are in a room that looks like it was used as a distillery of sorts.')

#room items ______________________
bottle1 = Object('bottle', 'third', 'this is an empty beer bottle', True, False, 'empty beer bottle')
bottle1.add_attribute('drink', 'there is nothing in this bottle! why would you try to drink it?')