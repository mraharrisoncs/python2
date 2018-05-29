tries = 0
password = ""
while password != "winter16" and tries < 3:
    password=input("Enter Password?")
    if password == "winter16":
        print("Access granted!")
    else:
        print("Access denied!")
        tries = tries + 1
        
          
    
