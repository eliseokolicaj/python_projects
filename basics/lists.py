color = ["red",'blue','green']
message = f" my favourite colour is {color[2].title()}"  #format string
print (message)


print (color[-1])										# prints the last element of list

color.append('yellow')									#add a element to the list in the end of list
print (color)

color[0] = 'white'										#change a particular element of the list using index
print(color)

color.insert(2,'black')									# insert a element in a particular index of the list
print(color)

del color[0]											#delete a particular element of list
print (color)											# cannot use this element anymore

popped_color = color.pop()								# pop() removes the last element of list
print(color)											# element popped can be used
print(popped_color)
print (f"The last colour we used is {popped_color.title()}.")

pop_color2 = color.pop(2)								#pop a particular element
print(f"popped color is {pop_color2}")
print(color)

color.remove ('blue')                                   #remove a element with a known value

color.append('white')
color.append('red')
color.append('blue')
print(color)

color.sort()											#sort a list permanently in alphabetic order
print(color)

color.sort(reverse=True)								#sorts the list in reverse alphabetic order
print(color)

print(sorted(color))									# sorted() sorts the list temporarily
print(color)

color.reverse()											#reverse permanently the order of list
print(color)

length_list=len(color)									# len() shows the lengh of list
print(f"the lengh of list is {length_list}")