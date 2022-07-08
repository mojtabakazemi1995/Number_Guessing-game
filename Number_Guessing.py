# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:57:55 2021

@author: Mojtaba
"""

import random
'''bazi hads adad '''
print('***Welcome to Number Guessing game!!! ***')
rand_num = random.randint(1, 100)
score = 100
in_number = '0'
count = 1


def checking_integer(arg) -> str:
    '''barresi integer boodan ya naboodan adad voroodi user'''

    try:
        int(arg)
        return arg
    except (ValueError, TypeError):
        return checking_integer(input('Enter integer number!!!: '))


def checkinig_range_number(arg) -> str:
    '''Barresi range adad voroodi user'''

    if 0 < int(arg) < 101:
        return arg
    else:
        arg = checking_integer(input('Enter a number between 1 to 100: '))
        return checkinig_range_number(arg)


def odd_or_even(num: int = rand_num) -> bool:
    '''Barresi zoj ya fard boodan Goal Number:
        if zoj -> True or fard -> False'''

    if num % 2 == 0:
        return True
    else:
        return False


def hint(val: int) -> str:
    '''Function tolid Hint'''

    if val == 1:
        if rand_num >= 50:
            print('''\nFirst chance
Hint1: Goal Number is Larger equals than 50!!!''')
        else:
            print('\nFirst chance \nHint1: Goal Number is smaller than 50!!!')
    elif val == 2:
        print('''\nSorry! Second chance
Baghimandeye taghsim Goal Number bar 9 barabar %d ast.'''
              % (rand_num % 9))
    elif val == 3:
        if odd_or_even() is True:
            print('\nSorry! Third chance \nGoal Number is Even')
        else:
            print('\nSorry! Third chance \nGoal Number is Odd')
    elif val == 4:
        print('''\nSorry! Last chance
Difference between your guess and Goal Number is %d''' % (abs(int(in_number) - rand_num)))


while int(in_number) != rand_num and score > 0:
    hint(count)
    print('Your score is %d' % (score))
    in_number = input('Enter your guess(as integer number between 1 to 100): ')
    in_number = checkinig_range_number(checking_integer(in_number))
    # barresi range va type voroodi user
    if rand_num == int(in_number):
        print('Congratulations!!! You win. Your score is %d' % (score))
    elif score > 25:
        count += 1
        score -= 25
    else:
        print('***Game Over***')
        score -= 25
