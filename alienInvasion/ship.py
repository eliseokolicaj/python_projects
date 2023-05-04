import pygame
from pygame.sprite import Sprite
from random import randint

class Ship(Sprite):
	"""A class to manage the ship."""

	def __init__(self,ai_game):
		"""Initialize the ship and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/spaceship.png')
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		# Store a decimal value for the ship's  position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flag
		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False


	def update(self):
		"""Update the ship's position based on movement flags."""
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.move_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		if self.move_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		## Update rect object from.
		self.rect.x = self.x
		self.rect.y = self.y

	def change_ship(self,ship_type):
		"""Change the apperence of the ship """
		ship_type = self.settings.random
		if ship_type == 1:
			self.image = pygame.image.load('images/ship2.png')
			self.rect = self.image.get_rect()
			## Update rect object from.
			self.rect.x = self.x
			self.rect.y = self.y
		elif ship_type == 2:
			self.image = pygame.image.load('images/ship3.png')
			self.rect = self.image.get_rect()
			## Update rect object from.
			self.rect.x = self.x
			self.rect.y = self.y

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


class ShipDisplay(Ship):
	"""Class to display small ships for the scoreboard"""
	def __init__(self,ai_game):
		super().__init__(ai_game)
		#change the image of ship
		self.image = pygame.image.load('images/spaceship1.png')







