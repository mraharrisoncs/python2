redtotal=0
red=[10,8,7,9,10,10,9,8,7,9]
for i in range(10):
  redtotal = redtotal + red[i]
# subtract max and min
print("red scores",redtotal)

bluetotal=0
blue=[17,9,6,8,7,4,10,8,7,9]
for i in range(10):
  bluetotal = bluetotal + blue[i]
bluetotal = bluetotal - max(blue) - min(blue) 
print("blue scores",bluetotal)
if bluetotal > redtotal:
    print("blue wins!")
elif bluetotal == redtotal:
    print("draw!")
else:
    print("red wins!")

print(max(red))
print(min(red))

    
