""" This program asks users for their name and registers their names in a file"""
display = "Please enter your name \n"
display += "Enter 'quit' to stop"
print(display)

loop = True
filename = 'guest_book.txt'

while loop:
	name = input("Name: ")
	if name != 'quit':
		print(f"Hello {name}!")
		with open(filename,'a') as file_object:
			file_object.write(f"{name.title()} visited this site! \n")
	else:
		loop = False
                                     
print ("Exiting...")