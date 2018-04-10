import sys
import time
import os


def print_step(string):
    print()
    print('***************************')
    print('*         ' + string + '         *')
    print('***************************')
    print()


def print_number(number):
    print('(' + str(number) + ')', end=' ')


def print_slowly(text):
    for i in text:
        print_number(i)
        sys.stdout.flush()
        time.sleep(0.3)


def addition():
    os.system('clear')
    print_step('Step-06')
    take = int(input('Enter your new total value: '))
    return take


def multiply():
    os.system('clear')
    print_step('Step-04')
    take = int(input('Enter your new total value: '))
    print('Now your value is: ', (take * 50))


def age_guessing_game_step_7():
    os.system('clear')
    print_step('Step-07')
    birth_day = int(input('Enter your Birth Year: '))
    total_value = int(input('Enter your total value: '))

    result = str(total_value-birth_day)

    os.system('clear')
    print_step('Result')

    if len(result) == 3:
        print('Your guess number is', result[0])
        age = result.lstrip(result[0])
        print('Your age is', age)
        print()
    else:
        print('Your guess number is', result[:2])
        age = result.lstrip(result[2:])
        print('Your age is', age)
        print()


def age_guessing_game_step_6_2():
    os.system('clear')
    print_step('Step-06')
    print_number('Add 1767 with your total number ')

    print()
    pick_up = input('Need calculator? (y/n) else you\'ll go to next step ').lower()
    print()

    if pick_up == 'y':
        take = addition()
        print('Now your value is', take + 1767)
        time.sleep(2)
        age_guessing_game_step_7()
    elif pick_up == 'n':
        age_guessing_game_step_7()
    else:
        age_guessing_game_step_6_2()


def age_guessing_game_step_6_1():
    os.system('clear')
    print_step('Step-06')
    print_number('Add 1768 with your total number')

    print()
    pick_up = input('Need calculator? (y/n) else you\'ll go to next step ').lower()
    print()

    if pick_up == 'y':
        take = addition()
        print('Now your value is', take + 1768)
        time.sleep(2)
        age_guessing_game_step_7()
    elif pick_up == 'n':
        age_guessing_game_step_7()
    else:
        age_guessing_game_step_6_1()


def age_guessing_game_step_5():
    os.system('clear')
    print_step('Step-05')
    pick_up = input('Have your birthday already passed in this year ? (y/n): ').lower()
    print()

    if pick_up == 'y':
        age_guessing_game_step_6_1()
    elif pick_up == 'n':
        age_guessing_game_step_6_2()
    else:
        age_guessing_game_step_5()


def age_guessing_game_step_4():
    os.system('clear')
    print_step('Step-04')
    print('Now multiply your new total by 50')
    print()
    pick_up = input('Need calculator? (y) else you\'ll go to next step ').lower()
    print()

    if pick_up == 'y':
        multiply()
        time.sleep(2)
        age_guessing_game_step_5()

    else:
        age_guessing_game_step_5()


def age_guessing_game_step_3():
        os.system('clear')
        print_step('Step-03')
        print('Now Add your number with 5')
        print()
        pick_up = input('Did you Add number? (y/n) ').lower()

        if pick_up == 'y':
            age_guessing_game_step_4()
        else:
            age_guessing_game_step_3()


def age_guessing_game_step_2():
    os.system('clear')
    print_step('Step-02')

    print('Now multiply your number with 2')
    print()
    pick_up = input('Did you multiply number? (y/n) ').lower()

    if pick_up == 'y':
        age_guessing_game_step_3()
    elif pick_up == 'n':
        age_guessing_game_step_2()
    else:
        age_guessing_game_step_2()


def age_guessing_game():
    os.system('clear')
    lis_t = []
    print_step('Step-01')

    print('Pick a number between 1-10:')

    for i in range(1, 11):
        lis_t.append(i)
    print_slowly(lis_t)
    print()

    pick_up = input('Did you pick up a number? (y/n) ').lower()

    if pick_up == 'y':
        age_guessing_game_step_2()
    elif pick_up == 'n':
        age_guessing_game()
    else:
        age_guessing_game()


if __name__ == '__main__':
    age_guessing_game()
