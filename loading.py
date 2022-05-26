#loading  messages
from typeEffect import type_effect
from time import sleep

error_message = 'Oops! It seems that something went wrong with what you typed. You will be redirected to make your last decision again.'
yes = ['yes','y']
no = ['no','n']

def ask_quit(): #done
    print()
    type_effect('Are you sure that you would like to quit? You will lose all progress. ')
    choice = input()
    choice = choice.lower()
    if choice in yes:
        print()
        loading('quit')
        quit()
    else:
        print()
        type_effect('Good choice. You will be redirected to make your last decision again')

def loading(message = 'loading'):
    if message == 'restart':
        message1 = 'SYSTEM RESTARTING... PLEASE STAND BY'
        message2 = 'REBOOT SUCCESSFUL'
        
    elif message == 'start':
        message1 = 'SYSTEM STARTING... PLEASE STAND BY'
        message2 = 'GAME BOOT SUCCESSFUL'

    elif message == 'quit':
        message1 = 'SYSTEM ENDING... PLEASE STAND BY'
        message2 = 'SYSTEM QUIT SUCCESSFUL'

    elif message == 'loading':
        message1 = 'SYSTEM LOADING... PLEASE STAND BY'
        message2 = 'SYSTEM LOAD SUCCESSFUL'

    elif message == 'saving':
        message1 = 'GAME SAVING... PLEASE STAND BY'
        message2 = 'GAME SAVE SUCCESSFUL'

    else:
        print('error')
        quit()

    print()
    type_effect(message1)
    sleep(2)
    print()
    type_effect('0%__________10%__________20%__________30%__________40%__________50%__________60%__________70%__________80%__________90__________100%')
    print()
    sleep(2)
    type_effect(message2)
    sleep(2)
    print()

def error(): #done
    print()
    type_effect(error_message)
    sleep(2)

def ask_restart(): #done
    print()
    type_effect('Are you sure that you would like to restart? You will lose all progress and be redirected back to the beginning of the game. ')
    choice=input()
    choice=choice.lower()
    if choice in yes:
        loading('restart')
    else:
        print()
        type_effect("If you did not want to restart, why did you type it? GAME CONTINUING... PLEASE STAND BY")