'''Room class. extremely bare bones and unfinished.'''

import sys
from time import sleep

class Room():
    def __init__(self, name='void', description='void'):
        self.name = name
        self.description = description

    def change_description(self, description):
        self.description = description