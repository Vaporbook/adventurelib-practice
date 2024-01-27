from adventurelib import *
from items import *
from player import *
from rooms import *

@when('look')
def look():
    print(player.current_room)

@when('go north', direction='north')
@when('go south', direction='south')
@when('go east', direction='east')
@when('go west', direction='west')
@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
@when('n', direction='north')
@when('s', direction='south')
@when('e', direction='east')
@when('w', direction='west')
def go(direction):
    
    print('Current room:')
    print(player.current_room)

    if not player.current_room.exit:
        breakpoint()
    
    room = player.current_room.exit(direction)
    if room:
        player.current_room = room

        print(f'You go {direction}.')
        look()

@when('eat ITEM')
def eat(item):
    obj = player.inventory.take(item)
    if not obj:
        print(f'You do not have a {item}.')
    else:
        print(f'You eat the {obj}.')

@when('inventory')
@when('inv')
def show_inventory():
    print('You have:')
    if not player.inventory:
        print('nothing')
        return
    for item in player.inventory:
        print(f'* {item}')

@when("frap")
@when("do frap")
def do_frap():
    say("""
        
        You begin to jump around while spinning in the air and
        making a woo-woo sound as you twiddle your thumbs and
        flex your toes.

    """)
    if player.current_room == south_room:
        say("""

            The noise and commotion and chaos of your frappery cause the little penguin to shiver, sneeze, and pop up on his mound of snow, where he starts dancing around and hopping vigorously, while making the same woo-woo sound you're making!

        """)
        penguin.awake = True
        penguin.status = 'wide awake and flapping and frapping around like a crazy bird.'
        city.status = 'disarray and the buildings are overgrown with vines and moss. Weeds are popping up through cracked sidewalks. Abandoned vehicles sit rusted by the road and there are no people anywhere.'
    player.energy = player.energy - 1

@when("wake penguin")
def wake_penguin():
    say("""

        No matter what you do, nothing seems to rouse this little guy from his restful slumber.

    """)

@when("look penguin")
def look_penguin():
    if player.current_room == south_room:
        penguin = player.current_room.items.find('penguin')
        if penguin:
            say(f'The penguin is {penguin.status}')

@when("look city")
def look_city():
    if player.current_room == east_room:
        city = player.current_room.items.find('city')
        if city:
            say(f'The city is {city.status}')