
reds =  [10,8,7,9,10,10,9,8,7,9]
blues = [17,9,6,8,7,4,10,8,7,9]

redtotal=0
for i in range(10):
  redtotal = redtotal + reds[i]
print("red scores",redtotal)

bluetotal=0
for i in range(10):
  bluetotal = bluetotal + blues[i]
print("blue scores",bluetotal)

if bluetotal > redtotal:
    print("blue wins!")
elif bluetotal == redtotal:
    print("draw!")
else:
    print("red wins!")

print(max(red))
print(min(red))

    
