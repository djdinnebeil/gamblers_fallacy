import random

def heads_or_tails():
    return ['heads', 'tails'][random.randint(0,1)]

if __name__ == '__main__':
    print(heads_or_tails())
