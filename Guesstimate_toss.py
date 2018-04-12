import random
import Guesstimate_age
import time
import os


def toss(team):
    os.system('clear')
    Guesstimate_age.print_step('  Toss ')
    toss = ['h', 't', 'h', 't']
    tossing = random.choice(toss)
    toss_input = input('Head or Tail (H/T): ').lower()

    if toss_input == 'h' or toss_input == 't':
        if tossing == toss_input:
            print(team, 'won the toss')
            time.sleep(1)

        elif tossing != toss_input:

            print(team, 'loss the toss')
            time.sleep(1)
    else:
        toss()


def select(team1, team2):

    Guesstimate_age.print_step('Match  ')
    print('Today the match between : ', team1, 'and', team2)
    print('Select (1) for ', team1)
    print('Select (2) for ', team2)

    select_team=int(input())
    if select_team == 1:
        print('you are ', team1)
        time.sleep(1)
        toss(team1)

    elif select_team == 2:
        print('you are ', team2)
        time.sleep(1)
        toss(team2)

    else:
        os.system('clear')
        select(team1, team2)


def match():
    team = ['SRH', 'KXIP', 'MI', 'RR', 'CSK', 'KKR', 'RCB', 'DD']
    team1 = random.choice(team)
    team2 = random.choice(team)
    while True:
        if team1 != team2:
            # print(team1)
            # print(team2)
            break
        else:
            team2 = random.choice(team)

    select(team1, team2)


if __name__ == '__main__':
    match()
