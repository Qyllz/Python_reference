import turtle

wn = turtle.Screen()
wn.title("Space Hockey Game!")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("orange")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("orange")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

hockey = turtle.Turtle()
hockey.speed(0)
hockey.shapesize(1.5)
hockey.shape("circle")
hockey.color("white")
hockey.penup()
hockey.goto(0, 0)
hockey.dx = 0.7
hockey.dy = 0.7

pen = turtle.Turtle()
pen.speed()
pen.color("#FFC0CB")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0 ", align="center", font=('Courier', 24, 'bold'))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)



wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")

while True:
    wn.update()

    hockey.setx(hockey.xcor() + hockey.dx)
    hockey.sety(hockey.ycor() + hockey.dy)

    if hockey.ycor() > 290:
        hockey.sety(290)
        hockey.dy *= -1

    if hockey.ycor() < -290:
        hockey.sety(-290)
        hockey.dy *= -1

    if hockey.xcor() > 390:
        hockey.goto(0, 0)
        hockey.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a,score_b), align="center", font=('Courier', 24, 'bold'))

    if hockey.xcor() < -390:
        hockey.goto(0, 0)
        hockey.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a,score_b), align="center", font=('Courier', 24, 'bold'))

    if 340 < hockey.xcor() < 350 and (paddle_b.ycor() + 50 > hockey.ycor() > paddle_b.ycor() - 50):
        hockey.setx(340)
        hockey.dx *= -1

    if hockey.xcor() < -340 and paddle_a.ycor() + 50 > hockey.ycor() > paddle_a.ycor() - 50:
        hockey.dx *= -1


