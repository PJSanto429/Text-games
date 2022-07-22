#imports---------------------
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

    print('---------------------main build(v 0.3.5)--------------------')
    print()
    introduction() #needs to be changed
    loading("start")
    player.room = 'first'
    text_input('look', player.room)
    
    while True: #live version of the game in version main
        print()
        text = input(">> ")
        text_input(text, player.room)