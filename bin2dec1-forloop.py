#Convert 4-bit binary to decimal - looped - Mr H

binaryNum = input("Enter a 4-bit binary number: ")
denaryAnswer = 0

for bit in range(0,3):
    placeValue = 2**(3-bit)
    if binaryNum[bit] == "1": 
        denaryAnswer = denaryAnswer + placeValue
print(binaryNum,"in denary is",denaryAnswer)


