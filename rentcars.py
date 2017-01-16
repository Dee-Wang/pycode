cars = ['Bens','BMW','Dazhong','Porsche']
car = input("Which car do you want to rent?")
if car.title() in cars:
	print("Find it, you can rent the car "+car.title())
else:
	print("Sorry, can't find it, please rent another car.")

