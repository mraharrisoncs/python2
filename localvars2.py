def display():
    name="Brian" # local variable, scope = display() function
    print("local name = ",name)
    
name = "Jeff" # global variable, scope = whole program
display()
print("global name = ",name)







