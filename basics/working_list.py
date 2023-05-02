names = ['goni','diu','vebiu']							
for name in names:										# for loop 
	print(f" {name.title()} is a ape")
	print(f" \t{name.title()} needs to be restrained")

print("Thank you ! \n")

for value in range(1,6):								# range() method in numerical list
	print(value)

numbers = list(range(1,6))								#list(range()) creates a num list
print(numbers)

numbers = list(range(1,15,3))								
print(numbers)

squares = []											#printing the square of numbers from 1-10
for num in range(1,11):
	squares.append(num**2)

print(squares)

#methods for lists
print(min(squares))
print(max(squares))
print(sum(squares))

#list comprehensions
squares = [ values**2 for values in range (1,11)]
print(squares)

#slicing a list (accessing elements from one index to another)
print(squares [0:4])
print(squares [:5])  #from 0 to index 4
print(squares [2:])  #from index2 to the last index

#looping in a list
print("\nhere are the numbers choosen:\n")
for value in squares [2:]:
	print(value)

#copying a list using slices
my_foods = ['banana','mango','apple','orange']
his_food = my_foods[:]
print(his_food)
my_foods.append("chiwi")
his_food.append('koko')

#Tuples = immutalbe list (unchangeable)
dimensions = (0,100,200)
for dimension in dimensions:
	print(dimension)


