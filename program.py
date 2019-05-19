"""Main call program"""

import quest_starters as aa
import vars as v
import sys


def main():
    print_header()
    print_instructions()
    aa.quest_one()
    aa.quest_two()
    aa.quest_three()
    aa.quest_four()
    aa.quest_five()
    if v.righty == 0:
        forest()
    elif v.righty == 1:
        cave()
    else:
        print('hallway no work')


def forest():
    # player chooses left hallway
    aa.quest_six()
    aa.quest_seven()
    aa.quest_eight()
    aa.quest_nine()
    aa.quest_ten()
    cave()


def cave():
    # player chooses right hallway initially or comes back
    aa.quest_eleven()
    aa.quest_twelve()
    aa.quest_thirteen()
    aa.quest_fourteen()
    aa.quest_fifteen()


def print_header():
    print('_________________________________________')
    print('             Text Adventure')
    print('_________________________________________')
    print()


def print_instructions():
    print('Here are the instructions for playing the game.')
    v.timing()
    print("Type only when you see a grammatical colon ':'.")
    v.timing()
    print("At any time, you can enter [options] to see what actions you can do.")
    v.timing()
    print("You also have an [inventory] and [stats] as well")
    v.timing()
    print('Have fun!')
    v.timing()
    print()
    print()


def restart():
    if v.dead is None:
        pass
    elif v.dead == "Y":
        v.dead = None
        main()
    elif v.dead == "N":
        sys.exit()


if __name__ == '__main__':
    main()
