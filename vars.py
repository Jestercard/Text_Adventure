"""Variable Reference List"""

"""main vars"""
options = []
inventory = []
quest = 0
turnaround = 0
dead = None

"""stats vars"""
health = 50
attack_power = 2
defense = 4

"""quest vars"""
mouth = 0  # sticking torch in mouth repeatedly
hallway = 0  # selecting to go down right hallway options
righty = 0  # fully committed to going down right hallway early
var2 = 0
var3 = 0


def timing():
    """adjust for delay in text"""
    import time
    time.sleep(.75)


def correct_answer():
    """advances to next quest by breaking the skeleton loop"""
    global quest
    quest = quest + 1


def reset(num):
    """resets the loop for the next quest, enter in current
    quest number, also clears out options"""
    global quest, turnaround
    quest = num
    turnaround = num
    options.clear()




'''
print('TEXTHERE')
v.timing()
'''
