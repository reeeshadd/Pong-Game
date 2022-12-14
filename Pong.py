import turtle
import winsound

# * game screen setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# * Score
score_a = 0
score_b = 0

# * Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # * animation speed, not paddle speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# * Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # * animation speed, not paddle speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# * Ball
ball = turtle.Turtle()
ball.speed(0) # * animation speed, not paddle speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#* Ball Movement
ball.dx = .08
ball.dy = -.08

# * Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("JetBrains Mono", 15, "normal"))


# * Paddle Movement Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if (y < 250):
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if (y > -250):
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if (y < 250):
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if (y > -250):
        y -= 20
        paddle_b.sety(y)

# * Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# * Main game loop
while True:
    wn.update()
    
    # * Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # * Top border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("collide", winsound.SND_FILENAME)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("collide", winsound.SND_FILENAME)
    
    # * Side check
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("JetBrains Mono", 15, "normal"))
        

        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("JetBrains Mono", 15, "normal"))
        

    
    # * Paddle & ball collision
    if (ball.xcor() > 340  and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce", winsound.SND_FILENAME)
    
    if (ball.xcor() <= -340  and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce", winsound.SND_FILENAME)