import random
import time

def eightball():
    answer = random.randint(1, 16)
    question = input("What is your question? ")
    time.sleep(2)
    print("Calculating.")
    time.sleep(2)
    print("Calculating..")
    time.sleep(2)
    print("Calculating...")
    time.sleep(4)
    print("Answer detected!")
    time.sleep(1)
    if answer == 1:
        print("Never in the whole, wide, world")
    if answer == 2:
        print("Yes, 100%")
    if answer == 3:
        print("Maybe, but not likely")
    if answer == 4:
        print("Don't get too excited, but yes")
    if answer == 5:
        print("No, sorry.")
    if answer == 6:
        print("Try again later")
    if answer == 7:
        print("Don't wake me up, I'll answer your question soon")
    if answer == 8:
        print("No.")
    if answer == 9:
        print("Yes, definitely")
    if answer == 10:
        print("50/50")
    if answer == 11:
        print("hahaha, no.")
    if answer == 12:
        print("looking positive")
    if answer == 13:
        print("decide for yourself!")
    if answer == 14:
        print("Yes :)")
    if answer == 15:
        print("High chance of a yes")
    if answer == 16:
        print("Don't think so :(")
    
    
