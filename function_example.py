def calc_cost(ticketprice, friends):
  return ticketprice * friends;

def calc_change(savings, cost):
  return savings - cost;

def show():
  print(concert,"tickets cost",cost)
  print("you have",change,"left");

concert = "Adele"
cost    = calc_cost(9.99,4)
change  = calc_change(100,cost)
show()


