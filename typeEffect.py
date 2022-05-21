#type effect

from time import sleep
import sys

def type_effect(text = ""):
    words = text
    for char in words:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()