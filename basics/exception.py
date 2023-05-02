""" Dealing with the  ValueError exception in a numerical input"""
print("Enter numbers to perform addittion")
print("Enter 'q' to exit")
while True:
	first_number = input("\nEnter first number : ")
	if first_number == 'q':
		break

	second_number = input("Enter second number : ")
	if second_number == 'q':
		break

	try:
		total_sum = int(first_number) + int(second_number)
	except ValueError:
		print("Please enter a number!")
	else:
		print(f"The sum is {total_sum}")