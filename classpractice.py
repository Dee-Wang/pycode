class Car():
	def _init__(self,car_brand,car_type):
		self.car_brand = car_brand
		self.car_type = car_type
	def drive(self):
		print("I am driving the car "+self.car_brand+" "+self.car_type+".")

my_car = Car('Audi','A6')
my_car.drive()

