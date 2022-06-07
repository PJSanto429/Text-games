#this is a save game function
import json
from time import sleep
import sys
from random import randint
from object import *
from typeEffect import type_effect
from loading import loading
from room import *
from encryptFile import fileCryption

def saveGame(player_room = 'none', version = 'main', code = 1234): #pretty much done
    print()
    type_effect('Would you like to create a new save file(1) or save to existing file(2)? ')
    choice = input()
    if choice == '2':
        print()
        type_effect('Please enter the code of the save file you would like to save to: ')
        code = input()
        try:
            fileCryption('decrypt', code)
        except:
            pass

        try:            
            with open(f'players/{code}.json', 'r') as infile:
                data = json.load(infile)

            if data[code][0]['password'] != 'none':
                print()
                type_effect('Please enter the password for this save file: ')
                choice = input()
                if choice == data[code][0]['password']:
                    name = data[code][0]['name']
                    writeFile(player_room, code, name, choice, version)

                else:
                    print()
                    type_effect('ERROR. Incorrect password. Please try again.')

            else:
                name = data[code][0]['name']
                writeFile(player_room, code, name, version)
        except:
            print()
            type_effect("I cannot find a save file with that code. Either you typed the wrong number, or you didn't save your game.")

    if choice == '1':
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
        writeFile(player_room, code, name, password, version)

def writeFile(player_room, code, name = 'none', password = 'none', newFile = True, version = 'main'):
    inventory = []
    items = []
    for i in Object.instances:  #adds to inventory list 
        if i.inInventory == True:
            inventory.append(i.longName)
        if i.longName != 'void':
            items.append(f'{i.longName}: {i.room}') #add more attributes to this(score, health, seen, etc.)

    data = {
        code:[
        {
            "name": name,
            "room": player_room,
            "password": password,
            "inventory": inventory,
            "items": items
            }
        ]
        }

    try:
        x = json.dumps(data)
        with open(f'players/{code}.json', 'w') as outfile:
            outfile.write(x)
            if version == 'main':
                loading('saving')
        fileCryption('encrypt', code)
    except:
        print()
        type_effect('ERROR. Something went wrong...')

def loadGame(version = 'main'): #done
    print()
    type_effect('Please type your savecode now: ')
    code = input()
    try:
        fileCryption('decrypt', code)
        with open(f'players/{code}.json', 'r') as infile:
            data = json.load(infile)
            #print(data['player1'][0]['name'])
        password = data[code][0]['password']
        
        if password != 'none':
            print()
            type_effect('Please enter the password for this save file: ')
            x = input()

            if x == password:
                if version == 'main':
                    loading('loading')
                room = data[code][0]['room']
                inventory = data[code][0]['inventory']
                items = data[code][0]['items']
                load = True
                #return code, room, inventory, items
            else:
                print()
                type_effect('Incorrect password')
                load = False

        else:
            if version == 'main':
                loading('loading')
            print()
            type_effect('load = good')
            room = data[code][0]['room']
            inventory = data[code][0]['inventory']
            items = data[code][0]['items']
            load = True
            #return room, inventory, items

        if load == True:
            items2 = []

            for i in items:
                i = i.split(':')
                i[1] = i[1].strip()
                items2.append(i)
                #print(i)
            item = items2

            print()
            for x, y in item:
                try:
                    for i in Object.instances:
                        if i.longName == x:
                            i.room = y
                            if y == 'inventory':
                                i.inInventory = True
                            else:
                                i.inInventory = False
                        else:
                            i.room = i.homeRoom
                except Exception as err:
                    #print(err)
                    pass

            '''for i in Object.instances:
                if i.longName in inventory:
                    i.inInventory = True
                    i.room = 'inventory'
                    player_inventory.append(i.longName)
                if i.longName in items: #work on this more
                    pass
                    #i.inInventory = False
                    #try:
                    #    player_inventory.remove(i.longName)
                    #except:
                    #    pass'''
            return room

    except Exception as err:
        #print(err)
        print()
        type_effect("I cannot find a save file with that code. Either you typed the wrong number, or you didn't save your game.")

def getRoom(code): #not currently being used(i think)
    with open(f'players/{code}.json', 'r') as infile:
        data = json.load(infile)
        room1 = data[code][0]['room']
        return room1

def getInventory(code): #not currently being used(i think)
    with open(f'players/{code}.json', 'r') as infile:
        data = json.load(infile)
        inventory = data[code][0]['inventory']
        return inventory