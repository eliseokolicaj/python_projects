

import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	filename = 'username.json'
	username = input("What is your name: ")
	with open(filename,'w') as f:
		json.dump(username, f)
	return username 

def greet_user():
	""" Greets the user."""
	username = get_stored_username()
	answer = input(f"Is this your username : {username}? (yes/no) ")
	if answer == 'yes':
		if username:
			print(f"Welcome back {username}!")
	elif answer == 'no':
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")
	else:
		print("Please answer with 'yes' or 'no'. \nEXITING...")

greet_user()