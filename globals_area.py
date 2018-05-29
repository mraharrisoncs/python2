# total area program

#constant declaration
pi=3.14159

def area_of_circle(r):
    area = pi * r**2
    return area

def area_of_square(s):
    area = s**2
    return area

# calculate the total area of many shapes
area = 0
area = area + area_of_circle(4)
area = area + area_of_square(7)
print("total area =",area)


