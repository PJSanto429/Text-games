#this is a save game function
import json
from time import sleep
import sys
from random import randint

def type_effect(text = ""):
    words = text
    for char in words:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

def saveGame(player_room):
    code = randint(1111, 9999)
    print()
    type_effect("Please enter a name for this save file: ")
    name = input()
    print()
    type_effect(f"Your code is {code}. Don't forget this, or you will not be able to get this save file.")
    print()
    type_effect("If you would like to add a password to this save file, please type it now. Otherwise, type NONE: ")
    password = input()

    data = {
    "player1":[
        {
            "name": name,
            "room": player_room,
        }
    ]
}
    try:
        x = json.dumps(data)
        with open(f'players/{code}.json', 'w') as outfile:
            outfile.write(x)
    except:
        pass

def loadGame(player_room, code = 0000):
    pass

  #this is a better way to read and write data for this game
data = {
    "player1":[
        {
            "name": 'btuh',
            "room": '2',
            "score": 'none',
        }
    ]
}

data2 = {
    "player2":[
        {
            "name": 'steve',
            "room": 'library',
            "score": 50,
            "access": 'user'
        }
    ]
}

x = json.dumps(data)
y = json.dumps(data2)

#with open('players/player1.json', 'w') as outfile:
#    outfile.write(x)

file1 = 'player1.json'

#with open (f'players/{file1}', 'r') as infile:
#    data = json.load(infile)
#    print(data['player1'][0]['name'])

    #getting items from a list in a dicitonary
    # https://pythonexamples.org/python-list-of-dictionaries/

    #python dictionaries and how to use them(refresher)
    # https://www.w3schools.com/python/python_dictionaries.asp
    
    # reading and writing to a json file
    # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/