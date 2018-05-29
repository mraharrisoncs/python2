import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
print(num1,"*",num2,"=?")
ans=float(input())
if ans == num1 * num2:
    print("correct!")
else:
    print("wrong")
