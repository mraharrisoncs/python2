# import the csv library module
import csv 

scores=[]
with open('scores.csv') as csvfile:
    scorefile = csv.reader(csvfile)
    for row in scorefile:
        scores.append(row)
        
print(scores)






        


    





    
