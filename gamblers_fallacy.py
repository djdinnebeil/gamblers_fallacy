import random

def roll_dice():
    """Simulates rolling two six-sided dice and returns their sum."""
    return random.randint(1, 6) + random.randint(1, 6)

def play_craps():
    """Plays a single round of Craps and returns the result."""
    # Come-out roll
    point = roll_dice()
    print(f"Come-out roll: {point}")

    if point in {7, 11}:
        print("Player wins!")
        return "win"
    elif point in {2, 3, 12}:
        print("Player loses!")
        return "lose"

    print(f"Point is set to {point}. Rolling until {point} or 7.")

    # Point phase
    while True:
        roll = roll_dice()
        print(f"Rolled: {roll}")

        if roll == point:
            print("Player wins!")
            return "win"
        elif roll == 7:
            print("Player loses!")
            return "lose"


if __name__ == '__main__':
    play_craps()
