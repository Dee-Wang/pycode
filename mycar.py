class Car():
	"""一次简单的模拟电动汽车的尝试"""
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_desc_name(self):
		long_name = str(self.year)+" "+self.make+" "+self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has "+str(self.odometer_reading)+" miles on it.")
	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading += mileage
		else:
			print("You can't roll back an odometer")
	def increment_odometer(self,miles):
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print("You can't roll back an odometer")

class ElectricCar(Car):
	def __init__(self,make,model,year):
		"""初始化父类的属性"""
		super().__init__(make,model,year)

my_tesla = ElectricCar('tesla','model S','2016')
print(my_tesla.get_desc_name())
