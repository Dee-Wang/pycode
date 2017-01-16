class Canguan():
	def __init__(self,canguan_name,cai_type):
		self.canguan_name = canguan_name
		self.cai_type = cai_type
		self.number_served = 0
	def describe_name(self):
		print("This is a canguan named "+self.canguan_name+" and the best cai here is "+self.cai_type+".")
	def open_canguan(self):
		print("The canguan "+self.canguan_name+" is open now.")
	def nrofcustomers(self):
		print("There are "+str(self.number_served)+" customers here.")
	def set_number_served(self):
		self.number_served = 10
	def increment_number_served(self,number_customers):
		self.number_served += number_customers
		

new_canguan = Canguan('laiyifen','Sichuan Food')
new_canguan.describe_name()
new_canguan.open_canguan()
new_canguan.nrofcustomers()
new_canguan.set_number_served()
new_canguan.nrofcustomers()
new_canguan.increment_number_served(20)
new_canguan.nrofcustomers()
