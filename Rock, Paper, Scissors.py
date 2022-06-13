import random

user_wins = 0
computer_wins = 0
no_one_won = 0

options = ['paper', 'scissors', 'rock']

while True:
    player = input('Choose an option: Paper, Scissors, Rock or Q to quit: ').lower()
    if player.lower() == 'q':
        break

    if player not in options:
        print('Invalid option')
        continue

    random_number = random.randint(0, 2)

# paper: 1, scissors: 2, rock: 3

    computer = options[random_number]
    print('Computer choosed', computer + '.')

    if player == 'paper' and computer == "rock":
        print('You Won! ')
        user_wins += 1

    elif player == 'scissors' and computer == 'paper':
        print('You Won! ')
        user_wins += 1

    elif player == 'rock' and computer == 'scissors':
        print('You Won! ')
        user_wins += 1

    elif player == computer:
        print('No one won')
        no_one_won += 1

    else:
        print('Your Lost! ')
        computer_wins += 1

print('You won', user_wins, 'times.')
print('Computer won', computer_wins, 'times.')
print('No one won', no_one_won, 'times.')

