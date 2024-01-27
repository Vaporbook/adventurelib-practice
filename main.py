import adventurelib
from adventurelib import *
from commands_asm import *
from rooms import *
from items import *
from player import *

def prompt():
    return '{hp} HP, {energy} EN > '.format(hp=player.hp, energy=player.energy)
adventurelib.prompt = prompt

print(entry_room.exits())

player.current_room = entry_room

look()

start()

