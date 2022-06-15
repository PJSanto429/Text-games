#this is a save game function
import json
from time import sleep, gmtime, strftime
import sys
from random import randint
from object import *
from typeEffect import type_effect
from loading import loading
from room import *
from encryptFile import fileCryption
from debugger import debug

def quit_save(player_room, version):
    currentTime = get_current_time()
    code, recentSaveTime = get_recent_save()

    for i in range(len(currentTime)):
        currentTime[i] = int(currentTime[i])
        recentSaveTime[i] = int(recentSaveTime[i])

    for i in range(len(currentTime)):
        if i != 4 and i != 5:
            if currentTime[i] > recentSaveTime[i]:
                do_quit_save(code, player_room, version)
                break
            #else:
            #    print(f'they are the same - {i}')
        if i == 4:
            if (currentTime[4]) >= (recentSaveTime[4] + 2):
                debug('minutes = different')
                do_quit_save(code, player_room, version)
                break
    
    fileCryption('encrypt', code)
    type_effect('Quitting...')
    quit()

def do_quit_save(code, player_room, version):
        #debug('wowee')
        print()
        type_effect(f'Would you like to save your game to file {code} before quitting? yes/no: ')
        choice = input()
        if choice in yes:
            saveGame(player_room, version, code)
            type_effect('Quitting...')
            quit()
        else:
            fileCryption('encrypt', code)
            type_effect('Quitting...')
            quit()

def get_current_time(): #this gets the current time
    time = strftime("%Y %m %d %H %M %S", gmtime()) #change this to another way(in todo.txt)
    time = time.split()
    return time

def get_save_time(code):
    try:
        fileCryption('decrypt', code)
    except:
        pass
    with open(f'players/{code}.json', 'r') as infile:
        data = json.load(infile)
    return data[code][0]['time']

def get_recent_save(): 
    savetime = []
    codes = []
    with open('players/saveCode.txt' ,'r') as saveCodes:
        data = saveCodes.read()
    data = data.split()
    for code in data:
        try:
            time = get_save_time(code)
            codes.append(code)
            savetime.append(time)
        except:
            pass
    for code in data:
        try:
            time = get_save_time(code)
            if time == (max(savetime)): #this is the most recent save time
                return code, max(savetime)
        except:
            pass

def times_played():
    with open('players/saveCode.txt', 'r') as infile:
        data = infile.read()
    print(data[1])

def auto_save(player_room = 'none', version = 'main', code = 1234):
    pass

def saveGame(player_room = 'none', version = 'main', code = 1234): #pretty much done
    with open('players/saveCode.txt', 'r') as infile:
        data = infile.read()
    data = data.split()
    if code in data:
        with open(f'players/{code}.json', 'r') as infile:
            data = json.load(infile)
        name = data[code][0]['name']
        password = data[code][0]['password']
        if password != 'none':
            #x = False
            while True:
                print()
                type_effect('Please enter the password for this save file: ')
                choice = input()
                if choice != password:
                    print()
                    type_effect('ERROR. Incorrect password. Please try again, or type EXIT to contiue the game where you left off')
                elif choice == password:
                    writeFile(player_room, code, name, version, password)
                    break
                elif choice == 'EXIT':
                    pass
        else:
            writeFile(player_room, code, name, version, password)
    else:
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
                        writeFile(player_room, code, name, version, choice)

                    else:
                        print()
                        type_effect('ERROR. Incorrect password. Please try again.')

                else:
                    name = data[code][0]['name']
                    writeFile(player_room, code, name, version, 'none')
            except:
                print()
                type_effect("I cannot find a save file with that code. Either you typed the wrong number, or you didn't save your game.")

        if choice == '1':
            if code == 0000:
                pass
            elif code == 1234:
                #goodCode = False
                while True:
                    code = randint(1111, 9999)
                    code = str(code)
                    try:
                        with open('players/saveCode.txt', 'r') as infile:
                            data = infile.read()
                        data = data.split()
                        if code not in data:
                            with open ('players/saveCode.txt', 'a') as outfile:
                                outfile.write(f' {code}')
                            break
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
            writeFile(player_room, code, name, version, password)

def writeFile(player_room, code, name = 'none', version = 'main', password = 'none'):
    items = []
    time = get_current_time()
    for i in Object.instances:  #adds to inventory list
        if i.longName != 'void':
            items.append(f'{i.longName}: {i.room}') #add more attributes to this(score, health, seen, etc.)

    data = {
        code:[
        {
            "name": name,
            "room": player_room,
            "time": time,
            "password": password,
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
            if version == 'dev':
                print('save successful')
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
            else:
                print()
                type_effect('load = good')
            room = data[code][0]['room']
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
                except:
                    pass

            return room

    except:
        print()
        type_effect("I cannot find a save file with that code. Either you typed the wrong number, or you didn't save your game.")

def getRoom(code):
    with open(f'players/{code}.json', 'r') as infile:
        data = json.load(infile)
        room1 = data[code][0]['room']
        return room1