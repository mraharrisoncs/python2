#Password Algorithm - Mr Harrison
import random # we need this to use randint

# set up lists
colourList = ["Red","Blue","Green"]
animalList = ["Tiger","Shark","Horse"]
puncList = ["%","£","&"]

# choose random values in lists
# randint(0,2) returns a random number 0,1,2
# NB. python counts from zero upwards!
colour = colourList[random.randint(0, 2)]
animal = animalList[random.randint(0, 2)]
punc = puncList[random.randint(0, 2)]

# make password and display it
password = colour + animal + punc
print("password =",password)





