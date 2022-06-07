#type effect

from time import sleep
import sys

def type_effect(text = ""):
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()