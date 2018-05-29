inRange=False
while inRange == False:
    ans=int(input("Please enter the % charge of your phone: "))
    if ans >= 0 and ans <= 100:
        inRange=True
print("Thank you for entering your phone charge level") 