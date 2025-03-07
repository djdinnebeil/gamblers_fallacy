import random
import logging

game_logger = logging.getLogger('GameLogger')
winnings_logger = logging.getLogger('WinningsLogger')

game_logger.setLevel(logging.WARNING)
winnings_logger.setLevel(logging.INFO)

# Create console handlers
console_handler = logging.StreamHandler()  # Sends logs to the console
console_handler.setLevel(logging.INFO)  # Ensures the handler logs INFO and above

# Define log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add handlers to loggers
game_logger.addHandler(console_handler)
winnings_logger.addHandler(console_handler)

def roll_dice():
    """Simulates rolling two six-sided dice and returns their sum."""
    return random.randint(1, 6) + random.randint(1, 6)

def play_craps():
    """Plays a single round of Craps and returns the result."""
    # Come-out roll
    point = roll_dice()
    game_logger.info(f'Come-out roll: {point}')

    if point in {7, 11}:
        game_logger.info('Player wins!')
        return 'win'
    elif point in {2, 3, 12}:
        game_logger.info('Player loses!')
        return 'lose'

    game_logger.info(f'Point is set to {point}. Rolling until {point} or 7.')

    # Point phase
    while True:
        roll = roll_dice()
        game_logger.info(f'Rolled: {roll}')

        if roll == point:
            game_logger.info('Player wins!')
            return 'win'
        elif roll == 7:
            game_logger.info('Player loses!')
            return 'lose'

def next_shooter():
    winnings = 0
    # play = input('Play next shooter (y for yes): ')
    total_shooters = 0
    while total_shooters < 10000:
        shooter = True
        shooter_round = 1
        while shooter:
            game_logger.info(f'Playing round {shooter_round}')
            if play_craps() == 'win':
                shooter_round += 1
            else:
                shooter = False
        game_logger.info(f'total rounds {shooter_round}')
        if shooter_round > 8:
            winnings -= 12800
            winnings_logger.info(f'*** loss *** current winnings: {winnings}')
        else:
            winnings += 25
            game_logger.info(f'current winnings: {winnings}')
        total_shooters += 1
        if total_shooters % 1000 == 0:
            winnings_logger.info(f'current winnings: {winnings}')
        # play = input('Play next shooter (y for yes): ')

if __name__ == '__main__':
    next_shooter()
