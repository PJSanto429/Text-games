from time import sleep
import sys
from colorama import init
from termcolor import colored

init() #colorama

def setInputText(text):
    inputText = text

allText = []
inputText = False
inputTextUsed = False
def type_effect(text = "", color = 'red', useGraphics = False, getInput=False):
    if not useGraphics:
        for char in text:
            sleep(0.04)
            #sys.stdout.write(char)
            try:
                sys.stdout.write(colored(char, color))
            except:
                sys.stdout.write(colored(char, 'red'))
            sys.stdout.flush()
    else:
        if getInput:
            inputText = text
        allText.append(text)