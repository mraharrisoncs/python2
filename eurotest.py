euroRate = 1.22

def euros(val):
    ans = val * euroRate
    return ans

poundval = float(input("Pounds?"))
euroval = euros(poundval)
print("That's",euroval,"Euros")
