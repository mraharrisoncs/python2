import turtle

def square():   # this function draws a square
    for i in range(4):
        turtle.right(90)
        turtle.forward(50)
        
def move(heading,steps):    # this shifts the turtle
    turtle.penup()
    turtle.setheading(heading)
    turtle.forward(steps)
    turtle.pendown()

def triangle():
    for i in range(3):
        # complete this triangle function
        # replace the word "pass" with some drawing code
        pass
        

#main program begins
key = "y"
while key == "y":
    move(90,50)
    square()
    key = input("again y/n?")
