import random

def roll_dice():
    """Simulates rolling two six-sided dice and returns their sum."""
    return random.randint(1, 6) + random.randint(1, 6)

def play_craps():
    """Plays a single round of Craps and returns the result."""
    # Come-out roll
    point = roll_dice()
    print(f'Come-out roll: {point}')

    if point in {7, 11}:
        print('Player wins!')
        return 'win'
    elif point in {2, 3, 12}:
        print('Player loses!')
        return 'lose'

    print(f'Point is set to {point}. Rolling until {point} or 7.')

    # Point phase
    while True:
        roll = roll_dice()
        print(f'Rolled: {roll}')

        if roll == point:
            print('Player wins!')
            return 'win'
        elif roll == 7:
            print('Player loses!')
            return 'lose'

def next_shooter():
    play = input('Play next shooter (y for yes): ')
    while play == 'y':
        shooter = True
        shooter_round = 1
        while shooter:
            print('Playing round', shooter_round)
            if play_craps() == 'win':
                shooter_round += 1
            else:
                shooter = False
        print('total rounds', shooter_round)
        play = input('Play next shooter (y for yes): ')

if __name__ == '__main__':
    next_shooter()
