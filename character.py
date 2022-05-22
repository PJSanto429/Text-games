#character class

class Character():
    def __init__(self, name = 'none', kind = 'none', room = 'none'):
        self.name = name
        self.kind = kind #different kids = enemy, shopkeep, thief, healer, etc.
        self.room = room #where they start(some will be able to move)