import turtle
#turtle.speed(1)

def square():   # this function draws a square
    for i in range(4):
        turtle.right(90)
        turtle.forward(50)

def triangle():   # this function draws a square
    for i in range(3):
        turtle.right(120)
        turtle.forward(50)

def move():
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()
    
#main program begins
print("drawing a square")
square()
move()
triangle()
move()
square()

print("finished!")
