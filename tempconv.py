#ask what conversion
ftoc=input("F to C?")
#if F to C
if ftoc=="Y":
# input temperature in F
    fah = int(input("fahrenheit?"))
# convert to C
    cel = (fah - 32) * 5 / 9
# display result
    print(cel,"celsius")
#else
else:
# input temperature in C
    cel = int(input("celsius?"))
# convert to F
    fah = cel * 9 / 5 + 32
# display result
    print(fah,"fahrenheit")
