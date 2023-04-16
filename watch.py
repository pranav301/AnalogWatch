
import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("this is my analog clock -  BY AJ")
wn.tracer(0)

# create drawing pen with attributes
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, S, pen):

    #draw clock face (circle)
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.down()
    pen.circle(210)
    pen.up()
    pen.goto(0, 250)
    pen.down()
    pen.circle(250)
    pen.up()
    pen.goto(0, 240)
    pen.down()
    pen.circle(240)
    pen.up()
    pen.goto(0, 190)
    pen.down()
    pen.circle(190)

    #draw lines for hours on clock
    pen.up()
    pen.goto(0,0)
    pen.setheading(90)

    for i in range(12):
        pen.fd(190)
        pen.down()
        pen.fd(20)
        pen.up()
        pen.goto(0, 0)
        pen.rt(30)

    #draw hour hand
    pen.up()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    pen.pensize(5)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.down()
    pen.fd(80)

    # draw minute hand
    pen.up()
    pen.goto(0, 0)
    pen.color("blue")
    pen.setheading(90)
    pen.pensize(5)
    angle1 = (m / 60) * 360
    pen.rt(angle1)
    pen.down()
    pen.fd(150)

    # draw second hand
    pen.up()
    pen.goto(0, 0)
    pen.color("Yellow")
    pen.setheading(90)
    pen.pensize(2)
    angle2 = (S / 60) * 360
    pen.rt(angle2)
    pen.down()
    pen.fd(145)

while True:
    h = int(time.strftime('%I'))
    m = int(time.strftime("%M"))
    S = int(time.strftime("%S"))

    draw_clock(h, m, S, pen)
    wn.update()

    time.sleep(1)

    pen.clear()


wn.mainloop()

