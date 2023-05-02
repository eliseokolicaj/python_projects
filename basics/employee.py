class Employee:
	"""Stores the name and salary of employees"""
	def __init__(self,name,last_name,salary):
		self.name = name
		self.last_name = last_name
		self.salary = salary

	def give_raise(self,raise1=None):
		if raise1:
			self.salary += raise1
		else:
			self.salary += 5000
		return (self.salary)



		