import pygame
from random import randint

class Background():
	"""A class to manage the background of Alien Invasion"""
	def __init__(self, ai_game):
		"""Initialize the background and set its starting position."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#Load the image of background
		self.image = pygame.image.load('images/galaxy4.png')
		self.rect = self.image.get_rect()

		#Set the rect of background 
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		""""Draw the background """
		self.screen.blit(self.image, self.rect)

	def change_background(self):
		"""Change the game background after killing alien fleet"""
		#Create a random number
		random_number = randint(1,4)
		if random_number == 1:
			self.image = pygame.image.load('images/galaxy2.png')
			self.rect = self.image.get_rect()
		elif random_number == 2:
			self.image = pygame.image.load('images/galaxy1.png')
			self.rect = self.image.get_rect()
		elif random_number == 3:
			self.image = pygame.image.load('images/galaxy4.png')
			self.rect = self.image.get_rect()
		else:
			self.image = pygame.image.load('images/galaxy3.png')
			self.rect = self.image.get_rect()
