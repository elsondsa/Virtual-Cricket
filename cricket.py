import random

while True:

    print('----WELCOME TO VIRTUAL CRICKET----')
    player1 = input('Enter name of player1:')
    player2 = input('Enter name of player2:')

    print("Any of you choose between heads and tails")
    choice = input('Choice of player1(heads/tails):')
    toss = random.randint(0,2)
    if toss==0:
        result = 'heads'
    else:
        result = 'tails'

    if result == choice:
        toss_win = player1
    else:
        toss_win = player2

    print('Its ',result,' and ', toss_win, 'has won the toss')

    choice = input('Enter the choice of the player(batting/bowling):')

    if (toss_win == player1) and (choice == 'batting'):
        first_play = player1
        second_play = player2
    elif (toss_win == player2) and (choice == 'batting'):
        first_play = player2
        second_play = player1
    elif (toss_win == player2) and (choice == 'bowling'):
        first_play = player1
        second_play = player2
    else:
        first_play = player2
        second_play = player1
    out = False
    score =0
    print(first_play, ' is going to bat')
    print('BATTING          BOWLING         SCORE')
    while out == False:
        bat = random.randint(0,6)
        bowl = random.randint(0,6)
        if bat == bowl:
            print(bat,'         ',bowl,'            ',score)
            out = True
            print(first_play, ' is out')
        else:
            score = score + bat
            print(bat,'         ',bowl,'            ',score)
            key = input()
    print('Total score of ',first_play,' is ',score)

    out = False
    score2 = 0
    print(second_play, ' is going to bat')
    print('BATTING          BOWLING         SCORE')
    while (out == False) and (score2 <= score):
        bat = random.randint(0,6)
        bowl = random.randint(0,6)
        if bat == bowl:
            print(bat,'         ',bowl,'            ',score2)
            out = True
            print(second_play, ' is out')
        else:
            score2 = score2 + bat
            print(bat,'         ',bowl,'            ',score2)
            key = input()
    print('Total score of ',second_play,' is ',score2)


    if score > score2:
        print(first_play,' wins')
    elif score == score2:
        print('Match is drawn')
    else:
        print(second_play, ' wins')

    choice = input('Want to play more?(yes/no):: ')
    if choice == 'yes':
        continue
    else:
        break
