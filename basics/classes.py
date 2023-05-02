#EXAMPLE 1 

class Restaurant:
	""" A simple example of a restaurant"""
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"The {self.name} restaurant is known for the {self.cuisine_type} cuisine")

	def open_restaurant(self):
		print("The restaurant is open")

	def increment_number_served(self,clients):
		self.number_served += clients

restaurant = Restaurant('Padam','traditional')
restaurant.number_served = 100
print(f"The number of clients served is {restaurant.number_served}")
print(f"The restaurant is called {restaurant.name}")
print(f"The restaurant cuisine is {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.increment_number_served(100)

print(f"Today {restaurant.number_served} clients have been served")


class IceCreamStand(Restaurant):
	"""Represent a restaurant specific to ice cream"""
	def __init__(self,restaurant_name,cuisine_type):
		""" Get the atributtes from parent class"""
		super().__init__(restaurant_name,cuisine_type)
		self.flavours = ['mango','chiwi','vanilla']

	def display_flavours(self):
		print("These are the ice cream flavours :")
		for flavour in self.flavours:
			print(flavour)

iceCream = IceCreamStand('China','chinese')
iceCream.display_flavours()
iceCream.describe_restaurant()


#EXAMPLE 2

class User:
	""" This is an example of a User class"""
	def __init__(self,first_name,last_name,gender,age,login_attempts):
		self.name = first_name
		self.surname = last_name
		self.gender = gender
		self.age = age
		self.login_attempts = login_attempts

	def describe_user(self):
		print(f"{self.name.title()} {self.surname.title()} is a {self.gender} and is {self.age} y old")

	def greet_user(self):
		print(f"Hello {self.name}!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0 

user_1 = User('gimi','fiqiriu','male',30,0)
user_2 = User('cimi','bedelli','female', 45,0)

print(f"This is {user_2.name.title()} {user_2.surname.title()} a {user_2.age} y old {user_2.gender}")
user_2.describe_user()
user_2.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"User 1 tried to login {user_1.login_attempts} times")

user_1.reset_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")


class Privilege:
	""" This class shows the privileges the admin has"""
	def __init__(self):
		self.privileges = ['can add post','can delete post','can ban user','can add user']

	def show_privileges(self):
		print("The admin can :")
		for privilege in self.privileges:
			print(privilege)


class Admin(User):
	""" This is a admin class"""
	def __init__(self,first_name,last_name,gender,age,login_attempts):
		super().__init__(first_name,last_name,gender,age,login_attempts)
		self.privileges = Privilege()

	
admin = Admin('gimi','fiqes','male',30,0)
admin.privileges.show_privileges()



#importing classes from modules: from module_name import class_name
#when importing entire module : import module_name
#creating instances: instance_name = module_name.class_name()
#importing all classes from module: from module_name import *


