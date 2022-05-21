#this is a save game function
import json
from time import sleep
import sys
from random import randint
from object import Object
from typeEffect import type_effect
from loading import loading

def saveGame(player_room = 'none', code = 1234): #pretty much done I THINK
    if code == 0000:
        pass
    else:
        code = randint(1111, 9999)
    print()
    type_effect("Please enter a name for this save file: ")
    name = input()
    print()
    type_effect(f"Your save code is {code}. Don't forget this, or you will not be able to get this save file.")
    print()
    type_effect("If you would like to add a password to this save file, please type it now. Otherwise, type NONE: ")
    password = input()
    password2 = password.lower()
    if password2 == 'none':
        password = 'none'

    inventory = []
    for i in Object.instances:  #adds to inventory list 
        if i.inInventory == True:
            inventory.append(i.longName)

    data = {
        code:[
        {
            "name": name,
            "room": player_room,
            "password": password,
            "inventory": inventory
            }
        ]
    }
    try:
        x = json.dumps(data)
        with open(f'players/{code}.json', 'w') as outfile:
            outfile.write(x)
    except:
        pass

def loadGame(): #close to being done
    print()
    type_effect('Please type your savecode now: ')
    code = input()
    try:
        with open(f'players/{code}.json', 'r') as infile:
            data = json.load(infile)
            #print(data['player1'][0]['name'])
        password = data[code][0]['password']
        
        if password != 'none':
            print()
            type_effect('Please enter the password for this save file: ')
            x = input()

            if x == password:
                name = data[code][0]['name']
                player_room = data[code][0]['room']
                inventory = data[code][0]['inventory']
                
                with open(f'players/{code}.json', 'r') as infile:
                    data = json.load(infile)
                inventory = data[code][0]['inventory']
                room1 = data[code][0]['room']
                loading('loading')
                return inventory, room1

            else:
                print()
                type_effect('Incorrect password')
    except:
        print()
        type_effect("I cannot find a save file with that code. Either you typed the wrong number, or you didn't save your game.")


def getInventory(code):
    with open(f'players/{code}.json', 'r') as infile:
        data = json.load(infile)
    inventory = data[code][0]['inventory']
    return inventory

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
            "inventory": ['cat', 'house', 'chair']
        }
    ]
}

x = json.dumps(data)
y = json.dumps(data2)

file1 = 'player1'

with open(f'players/{file1}.json', 'w') as outfile:
    outfile.write(y)


#with open (f'players/{file1}.json', 'r') as infile:
#    data = json.load(infile)
#x = data['player1'][0]['name']
#print(x)

    #getting items from a list in a dicitonary
    # https://pythonexamples.org/python-list-of-dictionaries/

    #python dictionaries and how to use them(refresher)
    # https://www.w3schools.com/python/python_dictionaries.asp
    
    # reading and writing to a json file
    # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/