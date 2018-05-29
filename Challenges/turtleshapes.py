import turtle

def square():   # this function draws a square
    for i in range(4):
        turtle.forward(50)
        turtle.right(90)
        
def shift():    # this shifts the turtle
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()

def triangle():
    for i in range(3):
        # complete this triangle function
        # replace the word "pass" with some drawing code
        pass
        

#main program begins
print("drawing a square")
square()

shift()

print("drawing a triangle")
# now call the triangle function here.

print("finished!")
