import pygame
from pygame.sprite import Sprite

class BlackHole(Sprite):
	"""Class to use to present black holes to upgrade the ship"""
	def __init__(self,ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load('images/black_hole.png')
		self.rect = self.image.get_rect()


		#Position the blackhole
		self.rect.x = 190
		self.rect.y = 230




