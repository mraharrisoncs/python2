# myEtchASketch application from Coding Club: Python Basics

from tkinter import *
import random

##### Set variables:
canvas_height = 400
canvas_width = 600
canvas_colour = "white"
p1_x=canvas_width/2
p1_y=canvas_height
line_width=5
line_length=5
colours=["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
maxcolour=6
p1_colour="green"

##### Functions:

# player controls
def p1_move_N(self):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, (p1_y-line_length), width=line_width, fill=p1_colour)
    p1_y = p1_y - line_length

def p1_move_S(self):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, p1_y+line_length, width=line_width, fill=p1_colour)
    p1_y = p1_y + line_length

def p1_move_E(self):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x + line_length, p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x + line_length

def p1_move_W(self):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x - line_length, p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x - line_length

def erase_all(self):
    canvas.delete(ALL)

##### procedure to change to random colour
def rand_colour(self): 
    global p1_colour
    rand_num = random.randint(0, maxcolour)
    p1_colour=colours[rand_num] 

#### procedure to set colour to green
def green(self): 
    global p1_colour
    p1_colour="green"

# usable colours are "white", "black", "red", "green",
#                    "blue", "cyan", "yellow", "magenta"
# write another procedure like "def green" to change colour to blue


##### main:
window = Tk()
window.title("MyEtchaSketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

# bind movement to key presses
window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Left>", p1_move_W)
window.bind("<Right>", p1_move_E)
window.bind("u", erase_all)
window.bind("c", rand_colour)
window.bind("g", green)

window.mainloop()
