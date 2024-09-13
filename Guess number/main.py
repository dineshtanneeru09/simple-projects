import random
def guess(a):
    rand = random.randint(1,a)
    guess = 0
    while guess != rand:
        guess = int(input(f'Guess a number between 1 and {a}:'))
        if guess<rand:
            print('Sorry, guess again. Two low.')
        elif guess>rand:
            print('Sorry, guess again. Two high.')
    print(f'Congrats.You have the right guess {rand}')
guess(10)