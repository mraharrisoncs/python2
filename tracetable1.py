fruits=['apple','banana','kiwi','pear','orange']
calories=[50,100,120,80,40]
title = "Fruit energy values"
print(title)
for num in range(5):
    currentFruit = fruits[num]
    currentCals = calories[num]
    if currentCals < 100:
        msg = "high!"
    else:
        msg = "low"
    print("Fruit {0} has {1} Calories which is {2}"
          .format(currentFruit,currentCals,msg))
print("Finished")
            
