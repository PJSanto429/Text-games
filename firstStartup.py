#this runs a simple command that creates a new folder for all save states to go into
from os import mkdir
try:
    mkdir('players') #don't change this or save/load game will not work properly
except:
    print('File already exists')