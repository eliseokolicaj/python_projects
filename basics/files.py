#Accessing content of a file

filename = 'learning_python.txt'

with open(filename) as file_object:
	content = file_object.read()
print(content)

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	if 'python' in line:
		print(line.replace('python', 'C').rstrip())
	else:	
		print(line.rstrip())
