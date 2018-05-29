ftoc=input("F to C?")
if ftoc=="Y":
    fah = int(input("fahrenheit?"))
    cel = (fah - 32) * 5 / 9
    print(cel,"celsius")
else:
    cel = int(input("celsius?"))
    fah = cel * 9 / 5 + 32
    print(fah,"fahrenheit")
    
