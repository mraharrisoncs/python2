# import the csv library module
import csv

def bubblesort(a,sortcol):
    count = len(a)
    for passes in range(count-1):
      swapped = False
      
      for num in range(count-1):
        if a[num+1][sortcol] < a[num][sortcol]:
            temp = a[num]
            a[num] = a[num + 1]
            a[num + 1] = temp
            swapped = True
            print(a)   
      if swapped == False:
        break
    return a

films=[]
with open('films.csv') as csvfile:
    f = csv.reader(csvfile)
    for row in f:
        films.append(row)
        
print(films)

sorted_films = bubblesort(films,0)
print(sorted_films)








 



  







        


    





    
