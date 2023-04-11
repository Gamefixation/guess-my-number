import os
import sys

os.environ['TERM'] = 'xterm'


small = 1
big = 100


while True:
    def clear():
        os.system('clear')

    def reset():
        global small
        global big

        small = 1
        big = 100

    def guess():
        hunch = (small + big - 1) >> 1
        clear()
        return hunch


    def smaller():
        global big
        big = guess() - 1


    def bigger():
        global small
        small = guess() + 1

    user_input = input(f'Is it {guess()}? ')

    if user_input == 'smaller':
        smaller()
    elif user_input == 'bigger':
        bigger()
    elif user_input == 'reset':
        reset()

    elif user_input == 'yes':
        user_input = input('Play again (yes/no)? ')
        if not user_input or user_input == 'no':
            sys.exit()
        reset()
