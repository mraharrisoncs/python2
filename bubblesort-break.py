# Mr Harrison - bubble sort program
a = [0,1,2,3,4,5,6,7,9,8]
count = 10
print(a) 

for passes in range(count-1):
  swapped = False
  
  for num in range(count-1):
    if a[num+1] < a[num]:
        temp = a[num]
        a[num] = a[num + 1]
        a[num+1] = temp
        swapped = True
        
  if swapped == False:
    break
    
print(a,passes+1)
      


