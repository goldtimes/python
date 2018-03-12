import random

secretNumber = random.randint(1,20)
print('I m thinking of number between 1 and 20.')
#只能猜6次
for i in range(1,7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('you guess is too low')
    elif guess > secretNumber:
        print('you guess is too high')
    else:
        break  #猜对了
if guess == secretNumber:
    print('Good job! you guessed my number in ' + str(secretNumber) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
