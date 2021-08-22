# whileLoops.py

# Loops allow Python and other programming languages to repeat
# simple behaviors many times in order to create more complex
# behaviors.

# two main types: for and while
import time


def printToX(x):
    val = 1
    while val <= x:
        print(str(val))
        val = val + 1
        time.sleep(2)
    return "Done!"


def threeGuesses():
    secretNumber = 69
    guess = False
    guesses = 3

    while guess == False and guesses > 0:
        ans = input("guess my secwet number UwU ")
        ans = int(ans)
        if ans == secretNumber:
            guess = True
        else:
            print("no u got it wrong LOL, guess again smh")
            guesses = guesses - 1
    if guess == True:
        print("pog you actually got it. now finish your homework lmao")
    else:
        print("bro you ran out of guesses.. go back to kindergarten")
    
def highOrLow():
    return None

def factorial(x):
    return None

def isItPrime(x):
    return None

def rollNDice(n):
    return None

