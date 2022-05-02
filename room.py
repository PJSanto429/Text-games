'''Room class. extremely bare bones and unfinished.'''

import sys
from time import sleep

def type_effect(text = ""): #typewriter effect. idk how it works
    words = text
    for char in words:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

class Room():
    def __init__(self, name='void', description='void', directions = 5):
        self.name = name
        self.description = description
        self.directions = directions

    def change_description(self, description):
        self.description = description

    def test(self):
        print()
        type_effect(f"Name: {self.name}")
        print()
        type_effect(f"Description: {self.description}")
        print()
        type_effect(f"Directions: {self.directions}")