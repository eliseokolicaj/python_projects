""" Dealing with the  FleNotFoundError in files"""
filename1 = 'dogs.txt'
filename2 = 'cats.txt'

try:
	with open(filename1, 'r') as file_object:
		contents = file_object.readlines()
except FileNotFoundError :
	print("File missing")
else:
	for content in contents:
		print(content)

try:
	with open(filename2, 'r') as file_object:
		contents = file_object.readlines()
except FileNotFoundError :
	pass
else:
	for content in contents:
		print(content)