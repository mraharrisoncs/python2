# A ten line chatbot in Python.
# Is this "AI"?

import random
greetings = ['hello', 'hi', 'hey!']
question = ['How are you?','You OK?']
responses = ['Good',"I'm fine"]

while True:
  userInput = input("Talk to me > ")
  if userInput in greetings:
    print(random.choice(greetings))
  elif userInput in question:
    print(random.choice(responses))
  else:
    print("Pardon?")
