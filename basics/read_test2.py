""" Reads the number from file fav_number.txt"""
import json
filename = 'fav_number.json'
with open(filename) as f:
	number = json.load(f)

print(number)