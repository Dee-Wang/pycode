class User():
	"""这是一个用户的简单的描述"""
	def __init__(self,first_name,last_name,age,city):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.city = city
		
	def greet_user(self):
		print("Hello, "+self.first_name+" "+self.last_name+".")
	def describe_name(self):
		print("This is "+self.first_name+" "+self.last_name+" and he is from "+self.city+". And he is "+self.age+" years old"+".")

new_user = User("Bob","Michael","27","Los Angles")
new_user.describe_name()
new_user.greet_user()
