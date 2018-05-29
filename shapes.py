import turtle
turtle.speed(0)
turtle.pensize(4)

def square(x,y,side,col,fill):   # this function draws a square
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(col)
    if fill:
        turtle.begin_fill()
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    if fill:
        turtle.end_fill()

def triangle(x,y,side,col,fill):   # this function draws a square
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(col)
    if fill:
        turtle.begin_fill()
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)
    if fill:
        turtle.end_fill()

def mycircle(x,y,rad,col,fill,arc):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(col)
    if fill:
        turtle.begin_fill()
    turtle.circle(rad,arc)
    if fill:
        turtle.end_fill()

def move(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

