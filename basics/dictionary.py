#Dictionary python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

#add new key-value pair 
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#modify values in the dictionary
alien_0['color'] = 'yellow'
print(alien_0['color'])

#example 
alien_1 ={'x_position': 0,'y_position': 25,'speed': 'medium'}
print(f"\nOriginial position is {alien_1['x_position']}")

if alien_1['speed'] == 'slow':
	x_increment = 1
elif alien_1['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"The new position of alien_1 is {alien_1['x_position']}")

#removing a key-pair 
del alien_0['points']
print(alien_0)

#using get() method to access value 
no_key = alien_0.get('name', 'alien_0 has no name')
print(no_key)

#looping through all key-value pairs
for key, value in alien_0.items():
	print(f"\nkey : {key}")
	print(f"value : {value}")

#loopin through all keys
for key in alien_0.keys():
	print(key.title())

#looping keys in a particular order 
for key in sorted(alien_0.keys()):
	print(key)
	print("\n")	

#looping through all values
for value in alien_0.values():
	print(value) 

#looping through unique values using set() method
for value in set(alien_0.values()):
	print(value)



