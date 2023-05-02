#positional arguments
def favourite_book(title,writer):
	"""Print a message"""
	print(f"one of my favourite books is {title.title()} written by {writer.title()}")

favourite_book('timi','koli')

#keyword arguments (name-value pair)
favourite_book(title = 'xoni',writer = 'diu')	

#return value
def formatted_name(first,last):
	format_name = f"{first} {last}"
	return format_name.title()

complete_name = formatted_name('ximi','neutron')
print(complete_name)

#function 
def make_album(name,title,songs = None):
	if songs:
		artist_album = {'artist_name': name, 'song_name': title,'number_songs': songs}
	else:
		artist_album = {'artist_name': name, 'song_name': title}
	return artist_album

artist = make_album('lymi','naploni',23)
print(artist)

#passing a list to a function
def greet_user(names):
	for name in names:
		msg = f"Hello {name.title()}"
		print (msg)

usernames = ['diu','gomi','keli']
greet_user(usernames)

#preventing a function from modifying a list (function_name(list_name [:]))

#example with list
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
sent_messages = []

def send_message(unprinted_designs,sent_messages):
	while unprinted_designs:
		unprinted_design = unprinted_designs.pop()
		print(f"Unprinted design is : {unprinted_design}")
		sent_messages.append(unprinted_design)
		
def show_message (sent_messages):
	for message in sent_messages:
		print(message)

send_message(unprinted_designs,sent_messages)
show_message(sent_messages)

#passing an arbitrary number of arguments using (*) (creates a tuple (unchangable list))
def make_pizza(*toppings):
	for topping in toppings:
		print(topping)
	

make_pizza('cheese','ananas')

#using arbitrary keyword arguments
def build_profile (first,last,**user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('koli','diu',rruga='orosh')
print(user_profile)

#importing an entire module : import module_name 
#then call a function: module_name.function_name()


#importing specific functions: from module_name import function_name_1,function_name_2 ...
#then call a function: function_name_1()

#Using "as" to Give a Function an Alias (nickname) : from module_name import function_name as function_nickname
#then call a function: function_nickname ()

#Using as to Give a Module an Alias : import module_name as module_nickname
#then call a function: module_nickname.function_name()

#Importing All Functions in a Module using (*): from module_name import *
#then call all functions by their name: function_name()