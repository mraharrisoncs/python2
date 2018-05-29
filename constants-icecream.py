#constants - these never change
conePrice = 1.50
tubPrice = 2.00

again="y"
while again == "y":
    print("Give me your icecream order..")
    print("cones are",conePrice,"tubs are",tubPrice)
#variables below - these change
    tubs=int(input("how many tubs?"))
    cones=int(input("how many cones?"))
    price=tubs*tubPrice + cones*conePrice
    print("price is",price)
    again=input("Another order (y/n)?")
print("Bye!")



