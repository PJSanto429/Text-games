#this is a save game function
import json
from time import gmtime, strftime
from random import randint
from object import *
from typeEffect import type_effect
from loading import loading
from room import *
from encryptFile import fileCryption
try:
    from debugger import debug
except:
    pass

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
        if i == 4:
            if (currentTime[4]) >= (recentSaveTime[4] + 2):
                debug('minutes = different')
                do_quit_save(code, player_room, version)
                break
    
    fileCryption('encrypt', code)
    type_effect('Quitting...')
    quit()

def do_quit_save(code, player_room, version):
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
        infile.close()
    return data[code][0]['time']

def get_recent_save(): 
    savetime = []
    codes = []
    with open('players/saveCode.txt' ,'r') as saveCodes:
        data = saveCodes.read()
        saveCodes.close()
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
        infile.close()
    print(data[1])

def saveGame(player_room = 'none', version = 'main', code = 1234): #pretty much done
    with open('players/saveCode.txt', 'r') as infile:
        data = infile.read()
        infile.close()
    data = data.split()
    if code in data:
        with open(f'players/{code}.json', 'r') as infile:
            data = json.load(infile)
            infile.close()
        name = data[code][0]['name']
        password = data[code][0]['password']
        #email = data[code][0]['email']
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
                    writeFile(player_room, code, name, version, password) #, email
                    break
                elif choice == 'EXIT':
                    pass
        else:
            writeFile(player_room, code, name, version, password) #, email
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
                    infile.close()

                if data[code][0]['password'] != 'none':
                    print()
                    type_effect('Please enter the password for this save file: ')
                    choice = input()
                    if choice == data[code][0]['password']:
                        name = data[code][0]['name']
                        #email = data[code][0]['email']
                        writeFile(player_room, code, name, version, choice) #, email

                    else:
                        print()
                        type_effect('ERROR. Incorrect password. Please try again.')

                else:
                    name = data[code][0]['name']
                    writeFile(player_room, code, name, version, 'none') #, (data[code][0]['email'])
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
                            infile.close()
                        data = data.split()
                        if code not in data:
                            with open ('players/saveCode.txt', 'a') as outfile:
                                outfile.write(f' {code}')
                                outfile.close()
                            break
                    except:
                        with open ('players/saveCode.txt', 'w') as outfile:
                            outfile.write('testCode')
                            outfile.close()
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
            #email = getEmail()
            writeFile(player_room, code, name, version, password) #, email

#this is not currently being used(might not ever be used)
def getEmail(email = 'none'): #this is a pretty simple thing to add but it is a bunch of little stuff that needs to be added - i dont really want to work on it righ tnor
    if email == 'none':
        print()
        type_effect('if you would like to receive an email with your save information, please enter your email now. otherwise, type none')
        email = input()
        if email.lower() == 'none':
            email = 'none'
    else:
        print()
        type_effect('please enter an email: ')
        email = input()
    return email

def writeFile(player_room, code, name = 'none', version = 'main', password = 'none', email = 'none'):
    items = []
    containers = []
    time = get_current_time()
    for i in Object.instances:  #adds to inventory list
        if i.longName != 'void' and i.room != 'void':
            items.append(f'{i.longName}: {i.room}|{i.parent}')
            if i.isContainer:
                containers.append(f'{i.longName}: {i.locked}|{i.containerKey}|{i.lockAbility}|{i.containerLimit}|{i.open}')
    
    data = {
        code:[
        {
            "name": name,
            "room": player_room,
            "time": time,
            "password": password,
            "items": items,
            "containers": containers
            }
        ]
        }
        
    try:
        x = json.dumps(data)
        with open(f'players/{code}.json', 'w') as outfile:
            outfile.write(x)
            outfile.close()
        if version == 'main':
            loading('saving')
            fileCryption('encrypt', code)
        if version == 'dev':
            print('save successful')
    except:
        print()
        type_effect('ERROR. Something went wrong...')

def loadGame(version = 'main'):
    print()
    type_effect('Please type your savecode now: ')
    code = input()
    try:
        fileCryption('decrypt', code)
    except:
        pass
    try:
        with open(f'players/{code}.json', 'r') as infile:
            data = json.load(infile)
            infile.close()
        password = data[code][0]['password']
    
        if password != 'none':
            debug('password == none')
            print()
            type_effect('Please enter the password for this save file: ')
            x = input()

            if x == password:
                if version == 'main':
                    loading('loading')
                room = data[code][0]['room']
                items = data[code][0]['items']
                try:
                    containers = data[code][0]['containers']
                except:
                    pass
                load = True
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
            try:
                containers = data[code][0]['containers']
            except:
                pass
            load = True
    except:
        pass
    try:
        if load == True:
            containers2 = []
            for i in containers:
                i = i.split(':')
                i[1] = i[1].strip()
                i[1] = i[1].split('|')
                containers2.append(i)
            containers = containers2
            #getting/setting all containers
            for x, y in containers:
                try:
                    for i in Object.instances:
                        if i.longName == x:
                            i.locked = y[0]
                            i.open = y[4]
                except:
                    pass
    except:
        pass
    try:
            items2 = []
            for i in items:
                i = i.split(':')
                i[1] = i[1].strip()
                i[1] = i[1].split('|')
                items2.append(i)
            item = items2
            #gettting/setting all items
            for x, y in item:
                try:
                    for i in Object.instances:
                        if i.longName == x:
                            i.room = y[0]
                            i.parent = y[1]
                            if y[0] == 'inventory':
                                i.inInventory = True
                            else:
                                i.inInventory = False
                        else:
                            i.room = i.homeRoom
                except:
                    pass
            
            return room
    except:
        #type_effect("I cannot find a save file with that code. Either you typed the wrong number, or you didn't save your game.")
        if version == 'main':
            lastSaveUpdate = 'July 7, 2022'
            type_effect(f"something went wrong with loading this game. if the save file was created before the {lastSaveUpdate} update, it might not be able to load")
        else:
            print()
            type_effect('something went wrong')


def getRoom(code):
    with open(f'players/{code}.json', 'r') as infile:
        data = json.load(infile)
        infile.close()
    room1 = data[code][0]['room']
    return room1