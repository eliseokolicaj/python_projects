# input () function
message = input("Tell me something :")
print(message)

#int () fumction for number inputs
age = input("Tell me your age : ")
age = int(age)
print(age)

#while loop and flags
prompt = "Do you wish to play?"
prompt += "Type 'quit' when you are finished"
active = True #FLAG
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)


#FILLING A DICTIONARY WITH USER INPUT
responses = {}
polling_active = True

while polling_active:
	name = input("Write your name :")
	response = input("What is your favourite bike?")

    #store the response in a dictionary
	responses[name] = response

	repeat = input("would you like for someone else to response?  (yes/no)")
	if repeat == 'no':
		polling_active = False

#Polling is finished \printing the result
print("Polling is finished")
for key,value in responses.items():
	print(f"{key} likes {value} bikes")