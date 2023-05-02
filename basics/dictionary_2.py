#CREATE A LIST OF DICTIONARIES
aliens = []

#make 30 green aliens 
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

#change the characteristics of aliens 
for alien in aliens [5:10]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'

#show the first 5 aliens 
for alien in aliens[:5]:
	print(alien)
print("...")

#show how many aliens are created
total_aliens = len(aliens)
print(f"There are {total_aliens} aliens created")


#A LIST IN A DICTIONARY
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t {topping}")

#DICTIONARY INSIDE DICTIONARY
users = {
'aeinstein': {
	'first': 'albert',
	'last': 'einstein',
	'location': 'princeton',
	},
'mcurie': {
	'first': 'marie',
	'last': 'curie',
	'location': 'paris',
	},
}

for user, user_info in users.items():
	print(f"\nUsername : {user.title()}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")