import getpass
import random
import sys
import time
import os


def print_step(string):
    print()
    print('***************************')
    print('*         ' + string + '         *')
    print('***************************')
    print()


def is_high_score(value):
    f = open('high_score.bat', 'r')
    current_high_score = f.read().split()[-1]
    f.close()
    if int(current_high_score) <= value:
        return True
    else:
        return False


def save_to_file(name, score):
    f = open('high_score.bat', 'w')
    f.write(name + ' ' + str(score))
    f.close()


def number_guessing_game(chances=10, high_value=100, l_no=1, mul_score=10,name=''):
    # name = input('Please enter your name: ')
    time.sleep(2)
    os.system('clear')
    name = name
    this_level_chances = chances
    hidden_number = random.randint(1, high_value+1)
    print(hidden_number)
    chances = chances + 1
    # print('Level:', l_no)
    print_step('Level-0'+str(l_no))

    while True:
        chances -= 1
        if chances == 0:
            print('Sorry', name, '! You lost.')
            print('See you next time!')
            print('The hidden number was', hidden_number)
            user_choice = input('Do you want to play again?(y/n): ')
            if user_choice == 'n':
                exit()
            else:
                number_guessing_game()
        print('You have', chances, 'chances left.')
        message = 'Try to Guess a number between 1 to ' + str(high_value) + ':'
        user_number = int(input(message))
        if hidden_number > user_number:
            print('Your guesses number is too low. Please try again...')
        elif hidden_number < user_number:
            print('Your guesses number is too high. Please try again...')
        else:

            if name == '':
                name = getpass.getuser()
                score = chances * mul_score

                print('Congratulation! You win.')
                print('Your score is', score)
                if is_high_score(score):
                    # name = input('Please enter your name: ')
                    print('welcome,', name, '. You made a new high score!')
                    save_to_file(name, score)
                    new_l_no = l_no + 1
                    print(name, ', You are now level', new_l_no)
                    new_chances = this_level_chances - 1
                    new_high_value = high_value + 20
                    new_score = mul_score + 5
                    number_guessing_game(chances=new_chances, high_value=new_high_value, l_no=new_l_no, mul_score=new_score, name=name)
            else:
                score = chances * mul_score

                print('Congratulation! You win.')
                print('Your score is', score)
                if is_high_score(score):
                    # name = input('Please enter your name: ')
                    print('welcome,', name, '. You made a new high score!')
                    save_to_file(name, score)
                new_l_no = l_no + 1
                print(name, ', You are now level', new_l_no)
                new_chances = this_level_chances - 1
                new_high_value = high_value + 20
                new_score = mul_score + 5
                number_guessing_game(chances=new_chances, high_value=new_high_value, l_no=new_l_no, mul_score=new_score, name=name)


if __name__ == '__main__':
    name = input('Please enter your name: ')
    number_guessing_game(chances=10, high_value=100, l_no=1, mul_score=10, name=name)
