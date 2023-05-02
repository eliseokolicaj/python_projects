""" Gets user favourite number if exist or ask for a new number"""
import json


filename = 'fav_number.json'

try:
	with open(filename,) as f:
		number = json.load(f)
except FileNotFoundError:
	number = input("Enter your favorite number: ")
	with open(filename, 'w') as f:
		json.dump(number, f)
		print("Next time we will remember your favourite number")

print(f"Your favourite number : {number}")

