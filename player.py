from adventurelib import *
from items import *

class Player:
    def __init__(self):
        self.inventory = Bag([])

    hp = 100
    energy = 100
    sagacity = 1
    level = 'Total Noob Dweeb'
    inventory.add(feather)
    inventory.add(pencil)

player = Player()

