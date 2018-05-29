# convert celsius to fahrenh.
def convertToCel(fah):
    cel = (fah - 32) * 5 / 9
    return cel

fah=int(input("Fahrenheit?"))
cel=convertToCel(fah)
print(cel,"Celsius")
