import math
import turtle
import random
import time

#x = -b +- (b^2 - 4ac)  /  2a

print("Hello, I am a calculator!")
print("Here is a list of things I can do!")
print("-------------------")
print("Quadform, diffofsquare, diffofcube, add, subtract, multiply, divide, exponent, sqrt, inum, convertv")


def qform(a, b, c):
    disc = sqrt((b ** 2) - (4*a*c))
    posnumerator = (-1 * b) + (disc)
    negnumerator = (-1 * b) - (disc)
    denominator = (2 * a)
    posquadans = (posnumerator) / (denominator)
    negquadans = (negnumerator) / (denominator)
    print("Formula: x = (-b +- √b^2 - 4ac)/(2a)")
    print("---------------------------")
    print("Discriminant: " + str(disc))
    print("Positive Numerator: " + str(posnumerator))
    print("Negative Numerator: " + str(negnumerator))
    print("Denominator: " + str(denominator))
    print("---------------------------")
    print("First Answer: " + str(posquadans))
    print("Second Answer: " + str(negquadans))
    
def diffofsquare(a, b):
    diffofsquareans = (a + b) * (a - b)
    print("Formula: a^2 - b^2 = (a+b)(a-b)")
    print("Answer: " + str(diffofsquareans))

def diffofcube(a, b):
    firstparen = (a - b)
    secondparen = ((a ** 2) + (a * b) + (b * b))
    diffofcubeans = (firstparen) * (secondparen)
    print("Formula: a^3 - b^3 = (a-b)(a^2 + ab + b^2)")
    print("Answer: " + str(diffofcubeans))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def exp(a, b):
    return a ** b


def equation():
    e = input("Write the equation here: ")
    print(eval(e))

def sqrt(a):
    return a ** 0.5

def div(a, b):
    return a/b

def convertv(a, b, c):
    print("Formula: f(x) = a(x-h)^2 + k")
    #steps: ax^2 + 8x + 7
    #steps: (2x^2 + 8x) + 7
    #steps: a(x^2 + 4x) + 7
    sign = "+"
    sign2 = "+"
    if b < 0:
        sign = ""
    if c < 0:
        sign2 = ""
    print("--------------")    
    print("f(x) = " + str(a) + "(x^2 " + str(sign) + str(b/a) + ") " + str(sign2) + str(c))


def inum(power):
    if (power%4) == 0:
        return 1
    if (power%4) == 1:
        return 'i'
    if (power%4) == 2:
        return -1
    if (power%4) == 3:
        return '-i'

def forms():
    print("Quadratic Formula: x = (-b +- √b^2 - 4ac)/(2a)")
    print("---------------------------")
    print("Vertex Form: f(x) = a(x - h)^2 + k")
    print("---------------------------")
    print("Standard Form: Ax + By = C")
    print("---------------------------")
    print("Point-slope Form: y - y1 = m(x - x1)")
    print("---------------------------")
    print("Slope-Intercept Form: y = mx + b")
    print("---------------------------")
    print("Difference of Squares: (x+y)(x-y)")

def sqrt4(a):
    return a ** 0.25

def sqrt3(a):
    return a ** 0.333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333



        

