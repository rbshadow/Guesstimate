import Guesstimate_age
import Guesstimate_number
import Guesstimate_emotion
import Guesstimate_toss as toss
import sys
import time
import os


def print_step(string):
    print()
    print('***************************')
    print('*         ' + string + '         *')
    print('***************************')
    print()


def print_slowly(text):
    for i in text:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(0.1)


def games():
    os.system('clear')
    print_step('Choose ')
    print('1 Guesstimate age ')
    print('2 Guesstimate number ')
    print('3 Guesstimate emotion ')
    print('4 Guesstimate toss ')
    choose = int(input())

    if choose == 1:
        time.sleep(1)
        if __name__ == '__main__':
            os.system('clear')
            Guesstimate_age.age_guessing_game()

    elif choose == 2:
        time.sleep(1)
        if __name__ == '__main__':
            os.system('clear')
            name = input('Please enter your name: ')
            Guesstimate_number.number_guessing_game(chances=10, high_value=100, l_no=1, mul_score=10, name=name)

    elif choose == 3:
        time.sleep(1)
        if __name__ == '__main__':
            os.system('clear')
            Guesstimate_emotion.emotion()
    elif choose == 4:
        time.sleep(1)
        if __name__ == '__main__':
            os.system('clear')
            toss.match()

    else:
        games()


if __name__ == '__main__':
    print()
    print_slowly('***************************')
    print()
    print_slowly('*  Welcome TO Guesstimate *')
    print()
    print_slowly('***************************')
    print()

    time.sleep(2)
    games()
