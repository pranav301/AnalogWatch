import turtle

wn= turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Triangle")

pen = turtle.Turtle()
pen.color("green")
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

while True:

    pen.up()
    pen.goto(-100, -80)
    pen.down()
    x=0

    for i in range(3):

        pen.setheading(x)
        pen.fd(200)
        x = x+120