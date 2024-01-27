from adventurelib import *
from items import *
from player import player

Room.add_direction('up', 'down')
# Room.add_direction('enter', 'exit')

entry_room = Room("""
==========
ENTRY ROOM
==========
                          
Whiz! Pop! Whirrrr!
    
Hello human!

Welcome to the BIG BIG adventure. If you've made it this far, you know how to invoke
the magical Python interpreter and you've successfully unlocked the ability to
run this program. Congrats, sage-seeker! Collect sage and solve puzzles to increase your
sagacity and get to new levels. If you find your way to the big treasure room,
you'll be glad you did!

Oh, and, uh -- got too much energy? You can always just frap to burn some of it off!

"""
+ f'Your level is: {player.level}'
)

south_room = Room("""
==========
SOUTH ROOM
==========
                  
You are in a very cold room, south of the entry room. It's like the north pole in here, so cold!

"""+
f'You see a penguin here, {penguin.status}')

# sleeping peacefully in the corner, on a pile of snow
# or
# wide awake and flapping and frapping around like a crazy bird
south_room.items = Bag([
   penguin,
])

east_room = Room("""
==========       
EAST ROOM
==========
                 
A hustling and bustling city! Could this be New York?

"""+                 
f'This city is in a state of {city.status}')

east_room.items = Bag([
   city,
])


west_room = Room("""
==========     
WEST ROOM
==========

This is the west room. You went west, nice job. This is so western feeling, not eastern at all.
""")

north_room = Room("""
==========
NORTH ROOM
===========

It's just like the north pole here! It's freezing and there's polar bears and igloos roaming around. Yes, the igloos themselves are roaming around. They actually have legs and they roam like Buffalo! Could it just be the polar bear inside of it?
""")

entry_room.north = north_room
entry_room.south = south_room
entry_room.east = east_room
entry_room.west = west_room
