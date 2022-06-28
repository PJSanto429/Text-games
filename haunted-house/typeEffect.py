#type effect

from time import sleep
import sys
from colorama import init
from termcolor import colored
init()

def type_effect(text = ""):
    for char in text:
        sleep(0.04)
        #sys.stdout.write(char)
        sys.stdout.write(colored(char, 'red'))
        sys.stdout.flush()