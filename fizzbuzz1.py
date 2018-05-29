for num in range(1,51):
    fizzorbuzz = False
    if num % 3 == 0:
	print("Fizz")
	fizzorbuzz = True
    if num % 5 == 0:
	print("Buzz")
	fizzorbuzz = True
    if not(fizzorbuzz):
	print(num)
