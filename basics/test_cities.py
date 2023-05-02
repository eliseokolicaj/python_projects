import unittest
from city_functions import city_country_name

class TestCityName (unittest.TestCase):
	""" Test for city_functions.py """
	def test_city_name (self):
		""""Test for just city name and country"""
		full_name = city_country_name('tirana','alabama')
		self.assertEqual(full_name,'Tirana,Alabama')

	def test_city_name_population(self):
		""" Test for city,country and population"""
		fullname = city_country_name('puka','albania','population=5000')
		self.assertEqual(fullname, 'Puka,Albania Population=5000')

if __name__ == '__main__':
	unittest.main()