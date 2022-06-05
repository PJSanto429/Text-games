#this runs a simple command that creates a new folder for all save states to go into
def firstStartup():
    from os import mkdir, path
    from cryptography.fernet import Fernet

    isExist = path.exists('players') #dont change this or save/load will not work
    if isExist == False:
        mkdir('players')
    isExist = path.exists('key.key')

    if isExist == False:
        key = Fernet.generate_key()
        with open('key.key', 'wb') as file: #DONT UNCOMMENT THIS OR THE KEY WILL CHANGE
            file.write(key)