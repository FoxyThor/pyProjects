import random

answer = random.randint(1,50)

print('Guess a number between 1 and 50')

guess = int(input('Take a guess. '))

while(guess<50):
    
    if(guess == answer):
        print('You win!')
        break
    elif(guess < answer):
        print('Too low!')
        guess = int(input('Guess again '))
    elif(guess > answer):
        print('Too high!')
        guess = int(input('Guess again '))
return
