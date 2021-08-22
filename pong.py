import turtle
 
#screen
screen = turtle.Screen()
screen.title("Pong game")
screen.bgcolor("white")
screen.setup(width=1000, height=600)
 
 
#Left paddle
left = turtle.Turtle()
left.speed(0)
left.shape("square")
left.color("black")
left.shapesize(stretch_wid=6, stretch_len=2)
left.penup()
left.goto(-400, 0)
 
 
#Right paddle
right = turtle.Turtle()
right.speed(0)
right.shape("square")
right.color("black")
right.shapesize(stretch_wid=6, stretch_len=2)
right.penup()
right.goto(400, 0)
 
 
#Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

#score
left_player = 0
right_player = 0
 
 
#shows score
score = turtle.Turtle()
score.speed(0)
score.color("blue")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))
 
 
#vertical
def paddleaup():
    y = left.ycor()
    y += 20
    left.sety(y)
 
 
def paddleadown():
    y = left.ycor()
    y -= 20
    left.sety(y)
 
 
def paddlebup():
    y = right.ycor()
    y += 20
    right.sety(y)
 
 
def paddlebdown():
    y = right.ycor()
    y -= 20
    right.sety(y)
 
 
#Keyboard
screen.listen()
screen.onkeypress(paddleaup, "w")
screen.onkeypress(paddleadown, "s")
screen.onkeypress(paddlebup, "Up")
screen.onkeypress(paddlebdown, "Down")
 
 
while True:
    screen.update()
 
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
 
    # Checking borders
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
 
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
 
    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player += 1
        score.clear()
        score.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 24, "normal"))
 
    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player += 1
        score.clear()
        score.write("Left_player : {}    Right_player: {}".format(
                                 left_player, right_player), align="center",
                                 font=("Courier", 24, "normal"))
 
    #collision
    if (ball.xcor() > 360 and
                        ball.xcor() < 370) and (ball.ycor() < right.ycor()+40 and ball.ycor() > right.ycor()-40):
        ball.setx(360)
        ball.dx*=-1
        
    if (ball.xcor()<-360 and
                       ball.xcor()>-370) and (ball.ycor()<left.ycor()+40 and ball.ycor()>left.ycor()-40):
        ball.setx(-360)
        ball.dx*=-1
