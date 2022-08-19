#this runs a simple command that creates a new folder for all save states to go into
def firstStartup():
    from os import mkdir, path
    from cryptography.fernet import Fernet
    if not path.exists('players'):
        mkdir('players')
    if not path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as file:
            file.write(key)
            file.close()