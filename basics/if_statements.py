cars = ['bmw','benz','toyota','audi']

cars.sort()
print(cars)

#checking for equality
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#checking for inequality
name ='gimi'
if name != 'xoni':
	print(f"The name's {name.title()}")

#checking if a value is in the list
if 'bmw' in cars:
	print("\nbmw")

#checking if a value is not in the list
if 'lambo' not in cars:
	print("Lambo not in the list")

# if-elif-else statement
age=13
if age < 4:
	print("Pay 0$")
elif age < 18:
	print("Pay 10$")
else:
	print("Go home")

#checking for a special value in list
for car in cars:
	if car =='bmw':
		print(f"{car}  is the most expensive car")
	else:
		print(car)

#checking if a list is not empty
if cars:
	print("List is not empty")