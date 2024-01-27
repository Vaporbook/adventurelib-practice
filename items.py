from adventurelib import *

class MaleCharacter(Item):
    subject_pronoun = 'he'
    object_pronoun = 'him'

inventory = Bag()

city = Item('bustling city', 'city')
city.status = 'hustling and bustling activity, a thriving hive of people going about their business.'

feather = Item('special feather', 'feather')
feather.type = 'turkey'

pencil = Item('ordinary pencil', 'pencil')
pencil.sharpened = False

penguin = MaleCharacter('cute penguin', 'penguin')
penguin.def_name = 'the penguin'
penguin.asleep = True
penguin.status = 'sleeping peacefully in the corner, on a pile of snow.'

potion_chill = Item('chill potion', 'chill potion')
