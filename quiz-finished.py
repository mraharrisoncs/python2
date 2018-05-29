import random
score=0
for i in range(5):
  num1=random.randint(1,10)
  num2=random.randint(1,10)
  answer=num1*num2
  print("What is",num1,"times",num2,"?")
  guess=int(input(">"))
  if guess==answer:
    print("Correct")
    score=score+1
  else:
    print("Incorrect")
print("You scored",score,"/5")
