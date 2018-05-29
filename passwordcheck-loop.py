password=input("Enter Password?")
newPassword = ""
while newPassword != password:
    newPassword=input("Enter Again?")
    if password == newPassword:
        print("Access granted!")
    else:
        print("Access denied!)
          
    
