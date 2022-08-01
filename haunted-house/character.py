from room import Room
from random import choice

class Character():
    instances = []
    def __init__(self, name = 'none', kind = 'none', room = 'none', movability = False, move_pattern = 'random'):
        self.__class__.instances.append(self)
        self.name = name
        self.move_pattern = move_pattern
        self.kind = kind #different kids = enemy, shopkeep, thief, doctor, etc.
        self.room = room #where they start(some will be able to move)
        self.movability = movability
        self.roomsToGo = []
        
    def add_rooms_to_go(self, rooms: list):
        for room in rooms:
            if room in Room.nameInstances and room not in self.roomsToGo:
                self.roomsToGo.append(room)
                
    def random_room_move(self):
        if self.movability:
            pass #this will access all rooms and make sure the character only moves to ones adjactent to it (in self.directions)