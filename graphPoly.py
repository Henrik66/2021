# graphPoly.py
# Name: Mr. Glenwerks
# March 3, 2017

########################################################
# Warning: Do not edit the code in this file. The
# changes made to this file can cause the graphing
# system to fail. This file should only be used by
# first importing it into another file where you are
# writing your own independent code. Use the:
# import graphPoly
# command to import this file, and then access its
# graphing functionality with commands including:
# graphPoly.graphLine([1, 1], "yellow")
# or
# graphPoly.graphPoly([1, -7, 12], "blue")
########################################################


















import turtle

scr = turtle.Screen()
scr.bgcolor("black")

cursor = turtle.Turtle()
cursor.shape("circle")
cursor.color("white")
cursor.turtlesize(0.5)
cursor.speed(10)

def createAxes(c):
    c.penup()
    c.goto(-500, 0)
    c.pendown()
    c.goto(500, 0)
    c.penup()
    c.goto(0, -500)
    c.pendown()
    c.goto(0, 500)
    c.penup()
    c.goto(0,0)

def createTics(c):
    c.penup()
    stops = range(-500, 500, 20)
    for stop in stops:
        c.goto(stop, 0)
        c.pendown()
        c.goto(stop, 10)
        c.goto(stop, -10)
        c.penup()
    for stop in stops:
        c.goto(0, stop)
        c.pendown()
        c.goto(10, stop)
        c.goto(-10, stop)
        c.penup()
    c.goto(0,0)
    
    
createAxes(cursor)
createTics(cursor)
def graphLine(lineList, newcolor="white", c=cursor):
    c.color(newcolor)
    ymin = lineList[0]*-500 + 20*lineList[1]
    ymax = lineList[0]*500 + 20*lineList[1]

    c.penup()
    c.goto(-500, ymin)
    c.pendown()
    c.goto(500, ymax)
    c.penup()
    c.goto(0,0)
    c.color("white")


def graphPoly(polyList, newcolor="white", c=cursor):
    c.color(newcolor)
    topPower = len(polyList)-1
    # Select X-values to graph over
    xs = range(-500, 501)
    ys = []
    # For each x-value, plug into the polynomial
    # to get the y-values
    for x in xs:
        cPower = topPower
        y = 0
        for coeff in polyList:
            if cPower == 0:
                y += 20*coeff
            else:
                y += 20**(-cPower+1)*coeff*x**cPower
            cPower -= 1
        ys.append(y)
    # initial cursor positioning
    c.penup()
    c.goto(xs[0], ys[0])
    c.pendown()
    # loop through each position and move the cursor
    # to those positions
    for i in range(len(xs)):
        if abs(ys[i]) <= 500 or i == len(xs)-1:
            c.goto(xs[i], ys[i])
    # reset cursor
    c.penup()
    c.goto(0,0)
    c.color("white")
        
