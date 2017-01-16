class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
	def increment_login_attempt(self):
		self.login_attempts += 1
	def reset_login_attempts(self):
		self.login_attempts = 0
		
my_user = User('Lily','Jenay')
while my_user.login_attempts < 5:
	my_user.increment_login_attempt();
print(my_user.first_name+" "+my_user.last_name+" "+str(my_user.login_attempts)+" times.")
my_user.reset_login_attempts()
print(my_user.first_name+" "+my_user.last_name+" "+str(my_user.login_attempts)+" times.")
