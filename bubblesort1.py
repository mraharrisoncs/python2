mylist = [1,7,3,9,6]
count = 5

print(mylist)

for passes in range(count-1, 1, -1):
  for item in range(passes):
    if mylist[item] < mylist[item + 1]:
        temp = mylist[item]
        mylist[item] = mylist[item + 1]
        mylist[item+1] = temp

print(mylist)
      


