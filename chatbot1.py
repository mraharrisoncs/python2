# Python Chatbot program - Mr Harrison

import random # we need the random functions

# Initialise arrays of greetings - you can edit these
hellos=['hello','hi!','howdy!'] # this is the "hellos" list
goodbyes=['goodbye!','bye!','see you!'] # this is the "goodbyes" list
nameResps=['Cool name',"Hey, that's my name!",'Suits you!']
colours=['red','blue','pink']
helloCount=len(hellos) # counts the number of elements in a list
goodbyeCount=len(goodbyes)
nameRespCount=len(nameResps)
colourCount=len(colours)
question=""

# Main Program Begins
print('Hi, this is chatbot Harry!')
name=input('What is your name? ')
response1 = hellos[random.randint(0,helloCount-1)]
print(response1,name)
col=input('What is your favourite colour {0}? '.format(name))
mycol=colours[random.randint(0,colourCount-1)]
if col == mycol:
    print('Wow! {0} is my favourite colour too!'.format(col))
elif col == 'black':
    print("I guess you're a Goth then!")
else:
    print('You like {0}, but I like {1} better.'.format(col,mycol))
    
while question != "bye":
    question=input('Ask any question, or say bye ')
    if question != "bye":
        print('Sorry, my programmer has not taught me',question)
goodbye=goodbyes[random.randint(0,goodbyeCount-1)]
print(goodbye)





