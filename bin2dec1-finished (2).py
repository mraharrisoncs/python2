#Convert 4-bit binary to decimal - Mr H

binaryNum = input("Enter a 4-bit binary number: ")
denaryAnswer = 0

if binaryNum[0] == "1": #note Python counts upwards from 0!
    denaryAnswer = denaryAnswer + 8
if binaryNum[1] == "1":  
    denaryAnswer = denaryAnswer + 4
if binaryNum[2] == "1":  
    denaryAnswer = denaryAnswer + 2
if binaryNum[3] == "1":  
    denaryAnswer = denaryAnswer + 1
print(binaryNum,"in denary is",denaryAnswer)


