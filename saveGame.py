#this is a save game function
import json
from time import sleep
import sys
from random import randint
from object import Object
from typeEffect import type_effect
from loading import loading

def saveGame(player_room = 'none', code = 1234): #pretty much done
    print()
    type_effect('Would you like to create a new save file(1) or save to existing file(2)? ')
    choice = input()
    if choice == '2':
        print()
        type_effect('Please enter the code of the save file you would like to save to: ')
        code = input()

        try:
            with open(f'players/{code}.json', 'r') as infile:
                data = json.load(infile)
            if data[code][0]['password'] != 'none':
                #add a way to check if there is a password when overwriting a save file
                print()
                type_effect('Please enter the password for this save file: ')
                choice = input()
                if choice == data[code][0]['password']:
                    pass
            else:
                pass
        except:
            pass
        loading('saving')

        writeFile(player_room, code)

    elif choice == '1':
        if code == 0000:
            pass
        elif code == 1234:
            goodCode = False
            while goodCode == False:
                code = randint(1111, 9999)
                code = str(code)

                try:
                    with open('players/saveCode.txt', 'r') as infile:
                        data = infile.read()

                    data = data.split()
                    for x in data:
                        if x != code:
                            with open ('players/saveCode.txt', 'a') as outfile:
                                outfile.write(f' {code}')
                            goodCode = True
                except:
                    with open ('players/saveCode.txt', 'w') as outfile:
                        outfile.write('testCode')

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
        else:
            pass
        #print(f'{name} {player_room} {code} {password}')
        writeFile(player_room, code, name, password)
        loading('saving')

def writeFile(player_room, code, name = 'none', password = 'none'):

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
        print()
        type_effect('ERROR. Something went wrong...')

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
                #loading('loading') #uncomment this for it to look better, but it takes too long during testing (same on line ~86)
                return code

            else:
                print()
                type_effect('Incorrect password')

        else:
            #loading('loading')
            return code
    except:
        print()
        type_effect("I cannot find a save file with that code. Either you typed the wrong number, or you didn't save your game.")

def getRoom(code):
    with open(f'players/{code}.json', 'r') as infile:
        data = json.load(infile)
    room1 = data[code][0]['room']
    return room1

def getInventory(code):
    with open(f'players/{code}.json', 'r') as infile:
        data = json.load(infile)
    inventory = data[code][0]['inventory']
    return inventory