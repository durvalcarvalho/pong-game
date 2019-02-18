import turtle
import os

# Window Setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("blue")
paddleA.shapesize(stretch_wid=5, stretch_len=0.8)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("green")
paddleB.shapesize(stretch_wid=5, stretch_len=0.8)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddleA_up():
	if(paddleA.ycor() + 20 < 260):
		paddleA.sety(paddleA.ycor()+20)

def paddleA_down():
	if(paddleA.ycor() - 20 > -260):
		paddleA.sety(paddleA.ycor()-20)

def paddleB_up():
	if(paddleB.ycor() + 20 < 260):
		paddleB.sety(paddleB.ycor()+20)

def paddleB_down():
	if(paddleB.ycor() - 20 > -260):
		paddleB.sety(paddleB.ycor()-20)

# Keyboard binding
wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")

wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")

# Main game loop
i=0
while True:
		
	i+=1 
	wn.update()

	if(i==7):
		i=0
		# Move the ball
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		# Border checking 

		# B Perdeu
		xcor = ball.xcor()
		if(xcor > 390):
			ball.goto(0, 0)
			ball.dx *= -1
			score_a += 1
			pen.clear()
			pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		
		# A Perdeu
		if(xcor < -390):
			ball.goto(0, 0)
			ball.dx *= -1
			score_b += 1
			pen.clear()
			pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

		ycor = ball.ycor()
		if(ycor > 290 or ycor < -290):
			ball.dy *= -1
		
	# Collisions

	if(ball.xcor()>340 and ball.xcor()<350 and 
	   ball.ycor() < paddleB.ycor()+40 and
	   ball.ycor() > paddleB.ycor()-40):
		ball.dx *= -1
		

	if(ball.xcor() < -340 and ball.xcor() > -350 and 
	   ball.ycor() < paddleA.ycor()+40 and
	   ball.ycor() > paddleA.ycor()-40):
		ball.dx *= -1
		
