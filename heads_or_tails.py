import random

def heads_or_tails():
    return ['heads', 'tails'][random.randint(0,1)]

def flip_coin(flips=1):
    """Flips a coin a set number of times"""
    tails_count = 0
    winnings = 0
    for _ in range(flips):
        side = heads_or_tails()
        if side == 'tails':
            tails_count += 1
        else:
            tails_count = 0
        if tails_count == 9:
            winnings -= 12800
            print(winnings)
        elif tails_count == 0:
            winnings += 25
            print(winnings)



if __name__ == '__main__':
    flip_coin(100000)
