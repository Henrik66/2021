# quiz1.py
# Name:
# Date: February 25, 2021

##################################################
# Part 1:
# Welcome to our first Python quiz! On this
# quiz, I have created four (4) functions.
# Your task is to complete any three (3) of
# those functions. If you choose to complete
# all four functions, only the first three
# will be graded. Each function is worth 6
# points, for a total of 18 points. Note that
# Function 2 has a bonus component, that is worth
# one bonus point.
##################################################


# Function 1: squirrelPlay(temp, is_summer)
# Squirrels love to play outside, but only when it
# is warm enough. On a normal day, squirrels will
# play outside if the temperature is between 60
# and 90 degrees. In the summer (is_summer == True),
# then squirrels will play outside if the
# temperature is between 60 and 100 degrees.
# Write a function that returns True if the
# squirrels would go out to play, given a temp
# (as a float) and a True/False statement
# of whether it is currently summer.
# Example: squirrelPlay(95.2, False)
#           returns False
#          squirrelPlay(95.2, True)
#           returns True
#          squirrelPlay(59.3, True)
#           returns False

def squirrelPlay(temp, is_summer):
    if is_summer == True and temp >= 60 and temp <= 100:
        return True
    if is_summer == True and temp <= 60 or temp >= 100:
        return False
    if is_summer == False and temp >= 60 and temp <= 90:
        return True
    if is_summer == False and temp <= 60 or temp >= 90:
        return False



# Function 2: collinear(pointA, pointB, pointC)
# This function should return True if the
# three given points, A, B, and C are all on the
# same line. It should return False otherwise.
# Each point is given as a two-element list:
# [x, y].

# Bonus (1 point): Design your function to also
# handle all cases involving points connected
# by vertical lines. NOTE: If your function
# can handle other cases but not this one, you
# will still receive regular full credit.

# Example: collinear([0,0], [1,1], [2,2])
#           returns True
#          collinear([0,0], [1,1], [2,4])
#           returns False
# Bonus:   collinear([1,1], [1,4], [2,6])
#           returns False
def collinear(pointA, pointB, pointC):
    slope1 = (pointB[1] - pointB[0] / pointA[1] - pointA[0])
    slope2 = (pointC[1] - pointC[0] / pointB[1] - pointB[0])
    if slope1 == slope2:
        return True
    else:
        return False

#this works as long as point A or B isn't 0, I ran out of time so I will just submit it


# Function 3: powersOfI(n)
# This function should return the value of
# the imaginary number, i, raised to the power
# of a given integer, n. You should use STRINGS
# for your return values: "i", "-1", "-i",
# and "1".
# Example: powersOfI(63)
#           returns '-i'
#          powersOfI(64)
#           returns '1'
#          powersOfI(-15)
#           returns 'i'
#def powersOfI(n):      I didn't do #3, only check 1, 2, 4
#    return None


# Function 4: isRACommonFactor(r, a, b):
# This function should determine whether or
# not the variable r is a common factor to
# both inputs a and b. Return True if r is a
# common factor, and return False otherwise.
# Example: isRACommonFactor(4, 12, 20)
#           returns True
#          isRACommonFactor(4, 12, 18)
#           returns False
#          isRACommonFactor(14, 28, 7)
#           returns False
def isRACommonFactor(r, a, b):
    if a % r == 0 and b % r == 0:
        return True
    else:
        return False



##################################################
# Part 2:
# In the following section, please compare and
# contrast the "=" and "==" commands in Python.
# Are these two commands interchangeable? Your
# explanation should be at least 2-3 sentences
# in length. (2 points)
# Make sure your answer is commented out!
##################################################
#
# = assigns values to variables
# while == checks whether or not both sides are equal. 
# For example, if you want to change the value of a variable you could
# do [variable] = [integer]. But if you wanted to check if something is 
# equal to something else you could do [something] == [something]
#
#
#
#
#
#
#
#
#
#
