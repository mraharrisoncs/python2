import random
answer = random.randint(1,11)
guess = 0
while guess != answer:
    guess = int(input("guess?"))
print("correct!")
