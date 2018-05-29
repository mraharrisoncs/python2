pi = 3.14157

def circ(r):
    c = 2 * pi * r
    return c

def area(r):
    a = pi * r**2
    return a

radius=int(input("radius?"))
print("area = ",area(radius))
print("circumference = ",circ(radius))

