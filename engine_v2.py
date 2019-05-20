"""Loop until correct answer is input"""

import quest_answers as bb
import vars as v

answer = None

verbs_how = []
verbs_where = ['run', 'walk', 'go', 'jog', 'look', ]
verbs_what = ['eat', 'chew', 'lick', 'use']


def skeleton():
    while v.quest == v.turnaround:
        global answer
        print()
        bb.checkhealth()
        if v.dead is None:
            answer = input('What do you do?:')
            answer = answer.lower().strip()

            while answer is not None:
                if answer == v.options[0]:
                    answer = None
                    print()
                    answer_a()
                elif answer == v.options[1]:
                    answer = None
                    print()
                    answer_b()
                elif answer == v.options[2]:
                    answer = None
                    print()
                    answer_c()
                elif answer == v.options[3]:
                    answer = None
                    print()
                    answer_d()
                elif answer == 'inventory':
                    answer = None
                    print()
                    print('Here is what you have in your inventory:')
                    v.timing()
                    if len(v.inventory) == 0:
                        print('There is nothing in your Inventory right now.')
                    else:
                        for c in v.inventory:
                            print('* {}'.format(c))
                    v.timing()
                elif answer == 'options':
                    answer = None
                    print()
                    print('Here are the following actions you can take:')
                    v.timing()
                    for c in v.options:
                        print('* {}'.format(c))
                    v.timing()
                elif answer == 'stats':
                    answer = None
                    print()
                    print('Here are your current stats')
                    v.timing()
                    print('* Health: {}'.format(v.health))
                    print('* Strength: {}'.format(v.attack_power))
                    print('* Armor: {}'.format(v.defense))
                    v.timing()
                elif answer in verbs_how:
                    print()
                    print("How do you want to {}?".format(answer))
                    answer = None
                    v.timing()
                elif answer in verbs_where:
                    print()
                    print("Where do you want to {}?".format(answer))
                    answer = None
                    v.timing()
                elif answer in verbs_what:
                    print()
                    print("What do you want to {}?".format(answer))
                    answer = None
                    v.timing()
                elif answer == 'debug':
                    print('quest is {}'.format(v.quest))
                    print('turnaround is {}'.format(v.turnaround))
                    break
                else:
                    print()
                    print("I don't understand what you mean by '{}.'".format(answer))
                    answer = None
                    v.timing()
        elif v.dead == 'Y':
            break
        else:
            print('Shutting down...')
            v.timing()
            break


def answer_a():
    if v.quest == 1:
        bb.quest_one_a()
    elif v.quest == 2:
        bb.quest_two_a()
    elif v.quest == 3:
        bb.quest_three_a()
    elif v.quest == 4:
        bb.quest_four_a()
    elif v.quest == 5:
        bb.quest_five_a()
    elif v.quest == 6:
        bb.quest_six_a()
    elif v.quest == 7:
        bb.quest_seven_a()
    elif v.quest == 8:
        bb.quest_eight_a()
    elif v.quest == 9:
        bb.quest_nine_a()
    elif v.quest == 10:
        bb.quest_ten_a()
    elif v.quest == 11:
        bb.quest_eleven_a()
    elif v.quest == 12:
        bb.quest_twelve_a()
    elif v.quest == 13:
        bb.quest_thirteen_a()
    elif v.quest == 14:
        bb.quest_fourteen_a()
    elif v.quest == 15:
        bb.quest_fifteen_a()
    else:
        pass


def answer_b():
    if v.quest == 1:
        bb.quest_one_b()
    elif v.quest == 2:
        bb.quest_two_b()
    elif v.quest == 3:
        bb.quest_three_b()
    elif v.quest == 4:
        bb.quest_four_b()
    elif v.quest == 5:
        bb.quest_five_b()
    elif v.quest == 6:
        bb.quest_six_b()
    elif v.quest == 7:
        bb.quest_seven_b()
    elif v.quest == 8:
        bb.quest_eight_b()
    elif v.quest == 9:
        bb.quest_nine_b()
    elif v.quest == 10:
        bb.quest_ten_b()
    elif v.quest == 11:
        bb.quest_eleven_b()
    elif v.quest == 12:
        bb.quest_twelve_b()
    elif v.quest == 13:
        bb.quest_thirteen_b()
    elif v.quest == 14:
        bb.quest_fourteen_b()
    elif v.quest == 15:
        bb.quest_fifteen_b()
    else:
        pass


def answer_c():
    if v.quest == 1:
        bb.quest_one_c()
    elif v.quest == 2:
        bb.quest_two_c()
    elif v.quest == 3:
        bb.quest_three_c()
    elif v.quest == 4:
        bb.quest_four_c()
    elif v.quest == 5:
        bb.quest_five_c()
    elif v.quest == 6:
        bb.quest_six_c()
    elif v.quest == 7:
        bb.quest_seven_c()
    elif v.quest == 8:
        bb.quest_eight_c()
    elif v.quest == 9:
        bb.quest_nine_c()
    elif v.quest == 10:
        bb.quest_ten_c()
    elif v.quest == 11:
        bb.quest_eleven_c()
    elif v.quest == 12:
        bb.quest_twelve_c()
    elif v.quest == 13:
        bb.quest_thirteen_c()
    elif v.quest == 14:
        bb.quest_fourteen_c()
    elif v.quest == 15:
        bb.quest_fifteen_c()
    else:
        pass


def answer_d():
    if v.quest == 1:
        bb.quest_one_d()
    elif v.quest == 2:
        bb.quest_two_d()
    elif v.quest == 3:
        bb.quest_three_d()
    elif v.quest == 4:
        bb.quest_four_d()
    elif v.quest == 5:
        bb.quest_five_d()
    elif v.quest == 6:
        bb.quest_six_d()
    elif v.quest == 7:
        bb.quest_seven_d()
    elif v.quest == 8:
        bb.quest_eight_d()
    elif v.quest == 9:
        bb.quest_nine_d()
    elif v.quest == 10:
        bb.quest_ten_d()
    elif v.quest == 11:
        bb.quest_eleven_d()
    elif v.quest == 12:
        bb.quest_twelve_d()
    elif v.quest == 13:
        bb.quest_thirteen_d()
    elif v.quest == 14:
        bb.quest_fourteen_d()
    elif v.quest == 15:
        bb.quest_fifteen_d()
    else:
        pass
