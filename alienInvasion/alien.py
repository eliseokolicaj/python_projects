import pygame
import numpy as np
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""
	
	def __init__(self,ai_game):
		"""Initialize the alien and set its starting position."""
		
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien image and set its rect attribute.
		self.image = pygame.image.load('images/alien3.png')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position.
		self.x = float(self.rect.x)

	def check_edges(self):
		""" Check if the alien hits the edges then return True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		""" Move the alien """
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x

		x_values = np.linspace(0, 2*np.pi,10)
		y_values = np.sin(x_values)
		for y_value in y_values:
			self.y = self.rect.y +  y_value
			self.rect.y = self.y 





