import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(height=600, width=600)

pen = turtle.Turtle()
pen.color("white")
pen.pensize(3)
pen.goto(0,0)
pen.setheading(90)
pen.speed(6)
pen.hideturtle()

while True:

    pen.goto(0, 0)
    pen.down()
    pen.goto(100,0)
    pen.setheading(90)
    pen.fd(100)
    pen.goto(0,100)
    pen.setheading(270)
    pen.fd(100)
    pen.setheading(90)

    pen.penup()
    pen.goto(-50, -50)
    pen.down()

    x=0
    for i in range(4):

        pen.setheading(x)
        pen.fd(200)
        x = x+90

    pen.up()


