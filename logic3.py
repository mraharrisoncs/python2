# logic error example 2
import random
answer = random.randint(1,10)
print("I am thinking of a number between 1 and 10")
guess=0
while guess != answer:
    guess=int(input("Guess?"))
    if guess == answer:
        print("Correct!")
    elif guess > answer:
        print("Higher!")
    else:
        print("Lower!")

           
