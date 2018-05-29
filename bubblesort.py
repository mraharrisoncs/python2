# Mr Harrison - bubble sort program
a = [1,7,3,9,6,2,4,8,5,0]
count = 10

print(a) 

for passes in range(count-1):
  for num in range(count-1):
    if a[num+1] < a[num]:
        temp = a[num]
        a[num] = a[num + 1]
        a[num+1] = temp

print(a)
      


