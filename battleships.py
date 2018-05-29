#battleships game

#setup the grid
grid=[[0,0,0,0,0],
      [0,0,0,0,0],
      [1,1,1,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]

#initialize "hits" variable
hits=
#initialize "shots" variable
shots=

#main loop
while hits < 3:
    #ask for guess
    guessRow=int(input("Row (0-5)?"))
    guessCol= 
    shots = shots + 1
    #check guess
    if grid[guessRow][guessCol]==1:
        print(
        hits = hits + 1

#hits = 3 so we are out of the loop
print("You win in",shots,"shots!")


