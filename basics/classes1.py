from random import randint

class Die:
	""""This class prints the radom number from the dice roll"""
	def __init__(self,sides=6):
		self.sides = sides

	def roll_die(self):
		random_number = randint(1,self.sides)
		print(f"The dice roll : {random_number}")

dice_6_sides = Die(20)
dice_6_sides.roll_die()
dice_6_sides.roll_die()
dice_6_sides.roll_die()