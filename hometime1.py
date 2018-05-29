again="y"
while again=="y":
    time=int(input("time?"))
    hours=time//100
    minutes=time%100
    minsLeft=15*60 - (hours*60+minutes)
    print("There are",minsLeft,"minutes left")
    again=input("Again? (y)")

    
