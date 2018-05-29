# import the csv library module
import csv 

scores=[]
with open('scores.csv') as csvfile:
    scorefile = csv.reader(csvfile)
    for row in scorefile:
        scores.append(row)
        
print(scores)
mtotal = 0
for student in scores:
  if student[1] == "f":
    mtotal = mtotal + int(student[3])
print("male total:",mtotal)





        


    





    
