import random
import sys

a = input("Wanna shoot some craps dawg? Enter 'y' for yes or 'n' for no\n")
if a.lower() == "n":
    sys.exit()
else:
    print("Lets go")
    
def diceNumber():
    
    _ = input("Press enter")
    
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    
    return (die1, die2)

def twoDice(both):
    die1, die2 = both
    print("Total of your roll is {} + {} = {}".format(die1, die2, sum(both)))
    
value = diceNumber()
twoDice(value)

diceTotal = sum(value)

if diceTotal in (7, 11):
    result = "You win"
    
elif diceTotal in (2, 3, 12):
    result = "You lose"
    
else:
    result = "Keep rolling"
    currentPoint = diceTotal
    print("Your point is", currentPoint, "Roll again")
    
while result == "Keep rolling":
    value = diceNumber()
    twoDice(value)
    diceTotal = sum(value)
    
    if diceTotal == currentPoint:
        result = "You win"
        
    elif diceTotal == 7:
        result = "You lose"
        
if result == "You win":
    print("We have a winner")
    
else:
    print("Loser")
    
    
    
    

    
    
    
    



    
    
    
    


    


    