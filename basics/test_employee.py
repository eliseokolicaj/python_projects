import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test for the class Employee"""
	def setUp(self):
		self.employee = Employee('gimi','fiqes',1000)

	def test_give_default_raise(self):
		annual_salary = self.employee.give_raise()
		self.assertEqual(annual_salary, 6000)

	def test_given_wanted_raise(self):
		annual_salary = self.employee.give_raise(1000)
		self.assertEqual(annual_salary, 2000)

if __name__ == '__main__':
	unittest.main()
