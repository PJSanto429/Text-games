#type effect

from time import sleep
import sys
from colorama import init
from termcolor import colored
init()

def type_effect(text = "", color = 'red'):
    for char in text:
        sleep(0.04)
        #sys.stdout.write(char)
        try:
            sys.stdout.write(colored(char, color))
        except:
            sys.stdout.write(colored(char, 'red'))
        sys.stdout.flush()