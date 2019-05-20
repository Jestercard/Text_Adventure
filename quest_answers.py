"""Possible paths and answers depending on what is typed"""

import vars as v


def checkhealth():
    """checks to see if dead"""
    if v.health > 0:
        pass
    else:
        print('You have run out of health points. You are dead.')
        v.timing()
        print('_________________________________________')
        print('             GAME OVER')
        print('_________________________________________')
        print()
        v.timing()
        v.dead = input('Do you wish to retry? Y/N:')


def quest_one_a():
    v.correct_answer()


def quest_one_b():
    print('You fall asleep on the cold rocky ground. Zzz...')
    v.timing()
    print('You wake up and once again see the light in the distance.')
    v.timing()


def quest_one_c():
    print('In your excitement, you accidentally run in to a wall. Ouch!')
    v.timing()
    print('Maybe if you knew where to run, that could help.')
    v.timing()


def quest_one_d():
    print('The faint light in the distance appears to be a lantern on a wall.')
    v.timing()
    print('Nothing else catches the eye')
    v.timing()


def quest_two_a():
    v.correct_answer()


def quest_two_b():
    print('You attempt to pick up the lantern.')
    v.timing()
    print('It does not budge. It seems to be fixed to the cave wall.')
    v.timing()


def quest_two_c():
    print('The fire is mesmerizing. Almost as if you want to touch it.')
    v.timing()
    print('Temptation fills your mind.')
    v.timing()


def quest_two_d():
    print('You reach out to touch the flame.')
    v.timing()
    print('As soon as your hand touches the heat, pain courses through your arm and you pass out.')
    v.timing()
    print('After some time, you awake and find yourself still in front of the lantern.')
    v.timing()


def quest_three_a():
    v.correct_answer()


def quest_three_b():
    print('Holding the stick with both hands, you smack it against the lantern.')
    v.timing()
    print('Aside from making a very loud metallic twang, this seemed to have no effect.')
    v.timing()


def quest_three_c():
    v.mouth = 1
    print('You put the stick in your mouth, however are unable to bite down into it.')
    v.timing()
    print('The stick tastes like wood.')
    v.timing()


def quest_three_d():
    print('The stick enters the flame, but is not able to catch fire.')
    v.timing()
    print('Maybe if there was something flammable nearby, that may help.')
    v.timing()


def quest_four_a():
    v.correct_answer()


def quest_four_b():
    if v.mouth == 1:
        print('You decide to further your weird mouth desire and shove the torch into your mouth again.')
        v.timing()
        print('It still tastes like wood.')
        v.timing()
    else:
        v.mouth = 2
        print('You put the torch into your mouth.')
        v.timing()
        print('It tastes like wood.')
        v.timing()


def quest_four_c():
    print('You look around the dark cave.')
    v.timing()
    print('Nothing else catches the eye.')
    v.timing()


def quest_four_d():
    print('You begin to walk into the darkness of the cave. Then you realize something.')
    v.timing()
    print('If there was a way to take the flame with you, that could help you see.')
    v.timing()


def quest_five_a():
    v.correct_answer()


def quest_five_b():
    if v.hallway == 0:
        v.options.clear()
        v.options.extend(['walk down left hallway', 'continue down right hallway', 'listen down hallways', 'eat torch'])
        print('You attempt to walk down the hallway only to be met with a cloud of bats!')
        v.timing()
        print('You stop as you witness the bats fly over you and down the hallway on the left.')
        v.timing()
        v.hallway = v.hallway + 1

    elif v.hallway == 1:
        print('Bats continue to pour out of the hallway.')
        v.timing()
        print('Maybe you should reconsider going down there.')
        v.timing()
        v.hallway = v.hallway + 1
    else:
        v.quest = v.quest + 1
        v.righty = 1


def quest_five_c():
    print('You listen down each hallway.')
    v.timing()
    if v.hallway == 0:
        print('The left one does not seem to have much sound coming from it.')
        v.timing()
        print('You can hear faint screeches down the right hallway.')
        v.timing()
    else:
        print('The sound of flapping and screeching can be heard as the bats fly about.')
        v.timing()
        print('No other sound catches your ear.')
        v.timing()


def quest_five_d():
    if v.mouth == 0:
        v.mouth = 1
        print('You put the torch in your mouth.')
        v.timing()
        print('The flame gets really close to your head.')
        v.timing()
        print('It tastes like wood.')
        v.timing()
        print('You remove the torch and hold it in front of you again.')
        v.timing()
    else:
        print('You lift the torch into your mouth yet again.')
        v.timing()
        print('Unsurprisingly, it tastes like wood and smells of smoke.')
        v.timing()
        print('You should probably stop putting things in your mouth.')
        v.timing()


def quest_six_a():
    print('You see a bunch of trees out in front of you.')
    v.timing()
    print('There is no discernible pathway.')
    v.timing()


def quest_six_b():
    if v.mouth == 0:
        v.mouth = 1
        print('You put the lit torch into your mouth. The flames dance close to your eyes.')
        v.timing()
        print('The torch leaves a woody after taste after you take it out of your mouth.')
        v.timing()
    elif v.mouth == 1:
        v.mouth = 2
        print('You look at the torch with a desire of a 2 year old and decide to taste it once more.')
        v.timing()
        print('It still tastes like wood.')
        v.timing()
    elif v.mouth == 3:
        v.mouth = 3
        print("Look, just because it's an option does not mean you should select this.")
        v.timing()
        print('Because guess what, it still tastes like wood.')
        v.timing()
    else:
        v.mouth = 4
        print("I'm done with your weird choices. It tastes like wood.")
        v.timing()


def quest_six_c():
    v.correct_answer()


def quest_six_d():
    print('You shout out at the top of your lungs in a desperate plea for aid.')
    v.timing()
    print('After waiting a few seconds, a wolf howls in the distance.')
    v.timing()
    print('No other sounds are heard nor signs of help appear')
    v.timing()


def quest_seven_a():
    pass


def quest_seven_b():
    pass


def quest_seven_c():
    pass


def quest_seven_d():
    pass


def quest_eight_a():
    pass


def quest_eight_b():
    pass


def quest_eight_c():
    pass


def quest_eight_d():
    pass


def quest_nine_a():
    pass


def quest_nine_b():
    pass


def quest_nine_c():
    pass


def quest_nine_d():
    pass


def quest_ten_a():
    pass


def quest_ten_b():
    pass


def quest_ten_c():
    pass


def quest_ten_d():
    pass


def quest_eleven_a():
    v.correct_answer()


def quest_eleven_b():
    pass


def quest_eleven_c():
    pass


def quest_eleven_d():
    pass


def quest_twelve_a():
    pass


def quest_twelve_b():
    pass


def quest_twelve_c():
    pass


def quest_twelve_d():
    pass


def quest_thirteen_a():
    pass


def quest_thirteen_b():
    pass


def quest_thirteen_c():
    pass


def quest_thirteen_d():
    pass


def quest_fourteen_a():
    pass


def quest_fourteen_b():
    pass


def quest_fourteen_c():
    pass


def quest_fourteen_d():
    pass


def quest_fifteen_a():
    pass


def quest_fifteen_b():
    pass


def quest_fifteen_c():
    pass


def quest_fifteen_d():
    pass
