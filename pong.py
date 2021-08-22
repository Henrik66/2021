import turtle
import time
 
# Create screen
screen = turtle.Screen()
screen.title("Pong game")
screen.bgcolor("white")
screen.setup(width=1000, height=600)
 
 
# Left paddle
left = turtle.Turtle()
left.speed(0)
left.shape("square")
left.color("black")
left.shapesize(stretch_wid=6, stretch_len=2)
left.penup()
left.goto(-400, 0)
 
 
# Right paddle
right = turtle.Turtle()
right.speed(0)
right.shape("square")
right.color("black")
right.shapesize(stretch_wid=6, stretch_len=2)
right.penup()
right.goto(400, 0)

 
# Ball of circle shape
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

time.sleep(5)