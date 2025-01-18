triangle=input("triangle(y) or rectangle(n)?")
if triangle == "y":
    base = int(input("base?"))
    height = int(input("height?"))
    area = base * height / 2
else:
    length = int(input("length?"))
    width = int(input("width?"))
    area = length * width
print("area = ",area)

    
    