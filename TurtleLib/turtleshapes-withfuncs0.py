import turtle

def square():   # this function draws a square
    for i in range(4):
        turtle.forward(50)
        turtle.right(90)
        
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
print("drawing a square")
square()
move(90,200)
square()
move(90,200)
square()

print("drawing a triangle")
# now call the triangle function here.

print("finished!")
