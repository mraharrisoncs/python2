# convert currency

#set constants
euroRate = 1.1
dollarRate = 1.22

#define functions
def euros(val):
    ans = val * euroRate
    return ans
def dollars(val):
    ans = val * dollarRate
    return ans


#main program begins
inVal = float(input("Amount in Pounds?"))
outVal = dollars(inVal)
print("£{0} in Dollars is ${1}".format(inVal,outVal))
