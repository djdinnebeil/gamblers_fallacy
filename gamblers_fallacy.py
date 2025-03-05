import random

def roll_dice():
    """Simulates rolling two six-sided dice and returns their sum."""
    return random.randint(1, 6) + random.randint(1, 6)

if __name__ == '__main__':
    print(roll_dice())