"""Quest starting points"""

from engine_v2 import skeleton
import vars as v


def quest_one():
    v.reset(1)
    v.options.extend(['run to light', 'sleep', 'run', 'look around'])
    v.inventory.extend(['cloth'])
    print('You wake up in a cave. It is dark, moist, and the sounds of water dripping can be heard.')
    v.timing()
    print('You have no clue how you got here. All you feel on your person is just the clothes on your back.')
    v.timing()
    print('In the distance, a faint light can be seen.')
    v.timing()
    skeleton()


def quest_two():
    v.reset(2)
    v.options.extend(['look around', 'pick up lantern', 'look into lantern', 'touch flame'])
    print('You run up to the light and see it is actually a metal lantern on the wall.')
    v.timing()
    print('The flame is in the open air. It is really bright now.')
    v.timing()
    skeleton()


def quest_three():
    v.reset(3)
    v.options.extend(['use cloth on stick', 'hit lantern with stick', 'eat stick', 'use stick on fire'])
    v.inventory.extend(['stick'])
    print('You notice a stick nearby resting against the wall.')
    v.timing()
    print('You add the stick to your inventory.')
    v.timing()
    skeleton()


def quest_four():
    v.reset(4)
    v.options.extend(['use torch on flame', 'eat torch', 'look around', 'walk'])
    v.inventory.clear()
    v.inventory.extend(['unlit torch'])
    print('You wrap the cloth onto the end of the stick.')
    v.timing()
    print('You now have a torch.')
    v.timing()
    skeleton()


def quest_five():
    v.reset(5)
    v.options.extend(['walk down left hallway', 'walk down right hallway', 'listen down hallways', 'eat torch'])
    v.inventory.clear()
    v.inventory.extend(['lit torch'])
    print('The torch bursts into flame and illuminates your nearby surroundings.')
    v.timing()
    print('The cave walls are wet and damp from an unknown source.')
    v.timing()
    print('There you notice you are actually in a hallway that forks to two directions.')
    v.timing()
    skeleton()


def quest_six():
    v.reset(6)
    v.options.extend(['look around', 'eat torch', 'run into forest', 'call for help'])
    print('You walk down the left hallway.')
    v.timing()
    if v.hallway != 0:
        print('The screeches from the bats grow fainter as you continue.')
        v.timing()
    print('Eventually, you are led to an opening to the outside world.')
    v.timing()
    print('The moon shines brightly and illuminates the surrounding forest.')
    v.timing()
    skeleton()


def quest_seven():
    v.reset(7)
    v.options.extend(['punch wolf', 'run into forest', 'kick wolf', 'cower in fear'])
    v.inventory.clear()
    v.inventory.extend(['burnt-out torch'])
    print('You run into the forest towards the moon in the sky.')
    v.timing()
    print('As you do so, you see a white flash next to you, but it soon disappears.')
    v.timing()
    print('All the running snuffs out your torch.')
    v.timing()
    print('Eventually, you come to a large clearing.')
    v.timing()
    print('But in front of you stands a white wolf!')
    v.timing()
    skeleton()


def quest_eight():
    v.reset(8)
    v.options.extend([])
    v.inventory.clear()
    v.inventory.extend([])
    print('Next quest text here')
    skeleton()


def quest_nine():
    v.reset(9)
    v.options.extend([])
    v.inventory.clear()
    v.inventory.extend([])
    print('Next quest text here')
    skeleton()


def quest_ten():
    v.reset(10)
    v.options.extend([])
    v.inventory.clear()
    v.inventory.extend([])
    print('Next quest text here')
    skeleton()


def quest_eleven():
    v.reset(11)
    v.options.extend([])
    print('Despite your better judgment, you head down the hallway of bats.')
    v.timing()
    print('right hallway worked!')
    skeleton()


def quest_twelve():
    v.reset(12)
    v.options.extend([])
    v.inventory.clear()
    v.inventory.extend([])
    print('Next quest text here')
    skeleton()


def quest_thirteen():
    v.reset(13)
    v.options.extend([])
    v.inventory.clear()
    v.inventory.extend([])
    print('Next quest text here')
    skeleton()


def quest_fourteen():
    v.reset(14)
    v.options.extend([])
    v.inventory.clear()
    v.inventory.extend([])
    print('Next quest text here')
    skeleton()


def quest_fifteen():
    v.reset(15)
    v.options.extend([])
    v.inventory.clear()
    v.inventory.extend([])
    print('Next quest text here')
    skeleton()
