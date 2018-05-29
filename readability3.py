def x():
  a = [1,7,3,9,6,2,4,8,5,0]
  c = 10;
print(a) 
for p in range(c-1):
  for num in range(c-1):
    if a[num+1] < a[num]:
        temp = a[num]
        a[num] = a[num + 1]
        a[num+1] = temp
print(a)
      


