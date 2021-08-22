# FunctionsDay2.py
# Name: Henrik
# Date:

# Some functions for us to build today:
def isItEven():
    num = int(input("Enter any number: "))
    if (num % 2) == 0:
        print("{0} is an Even number".format(num))
    else:
        print("{0} is an Odd number".format(num))
    # Your code here: should return True
    # if x is an even number, and should
    # return False otherwise.
    return None

def isNAFactor(x, n):
    num = int(input("Enter what should be factored: "))
    num2 = int(input("Enter the factor:"))
    if (num % num2) == 0:
        print("{0} is a facter of your number".format(num))
    else:
        print("{0} is not a factor of your number".format(num))
    # Similar to above, should return True
    # if n is a factor of x, and should
    # return False otherwise.
    return None

def medianOfThree(a, b, c):
    a = int(input("Input the first number: "))
    b = int(input("Input the second number: "))
    c = int(input("Input the third number: "))
    if b < a and a < c:
        print(a)
    elif c < a and a < b:
        print(a)
    elif c < b and b < a:
        print(b)
    elif a < b and b < c:
        print(b)
    elif b < c and c < a:
        print(c)
    elif a < c and c < b:
        print(c)
    # Should return the median value of
    # the three numbers given, a, b, or c.
    return None

def medianOfFour(a, b, c, d):
    # A bit trickier, now you need to find
    # the median of FOUR numbers, which
    # will be the average of the middle two
    # numbers...
    return None

def areaOfTrapezoid(b1, b2, h):
    # Given the two bases and height of a
    # trapezoid, return its area.
    return None

def areaOfShape():
    # The challenge problem today! Using
    # input commands, determine which shape
    # the user wants to calculate the area of
    # (can start with triangle, rectangle, and
    # circle for instance), and then ask the
    # user for the measurements needed for the 
    # appropriate formula (so for triangle, ask
    # for the base and the height). Perform the
    # associated formula, and return the result!
    return None
