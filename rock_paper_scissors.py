import random

def rps():   # rock paper scissors
    user_wins = 0
    computer_wins = 0
    games = 0
    game_max = 5
    options = ['rock', 'paper', 'scissors']

    while games < game_max:
        user_pick = input('Pick either rock, paper or scissors:\n').lower()

        random_number = random.randint(0,2)
        computer_pick = options[random_number]
        print(f'The computer picked {computer_pick}.\n')

        if user_pick not in options:
            continue             # will continue back to the top

        if user_pick == computer_pick:
            print(f'You both picked {user_pick}. Try again!\n')
        elif user_pick == 'rock' and computer_pick == 'scissors':
            user_wins += 1
            games += 1
            print('You Win!\n')
            print(f'You have {user_wins} win(s).')
            print(f'the computer has {computer_wins}.')
        elif user_pick == 'paper' and computer_pick == 'rock':
            user_wins += 1
            games += 1
            print('You Win!\n')
            print(f'You have {user_wins} win(s).\n')
            print(f'the computer has {computer_wins}.')
        elif user_pick == 'scissors' and computer_pick == 'paper':
            user_wins += 1
            games += 1
            print('You Win!\n')
            print(f'You have {user_wins} win(s).\n')
            print(f'the computer has {computer_wins}.')
        else:
            computer_wins += 1
            games += 1
            print(f'The computer picked {computer_pick}.\n')
            print('You Lost!\n')
            print(f'the computer has {computer_wins} win(s).')
            print(f'You have {user_wins}.\n')
    
    if user_wins > computer_wins:
        print(' Y O U  W O N !!!\n')
        print(f'You had {user_wins} and the computer had {computer_wins}.\n')
        quit()
    else:
        print(' Y O U  L O S T !!!\n')
        print(f'The computer had {computer_wins} and you had {user_wins}.\n')
        quit()




rps()