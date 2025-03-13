import random

def heads_or_tails():
    return ['heads', 'tails'][random.randint(0,1)]

def flip_coin(flips=1):
    for _ in range(flips):
        print(heads_or_tails())

if __name__ == '__main__':
    flip_coin(10)
