from random import randint

class Settings:
	"""A class to store all settings for Alien Invasion."""
	
	def __init__(self):
		"""Initialize the game's settings."""
		self.screen_width = 1366
		self.screen_height = 700
		self.bg_color = (0, 0, 0)

		#Ship settings
		self.ship_speed = 1.5
		self.ships_limit = 3
		#Ship type 
		self.ship_type = 2

		#Bullet setings
		self.bullet_speed = 3.0
		self.bullet_height = 8
		self.bullet_width = 400
		self.bullet_color = (230, 230, 230)
		self.bullets_allowed = 3

		#Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		#Speed up scale for aliens
		self.speed_scale = 1.1
		self.initialize_dynamic_settings()
		self.initialize_normal_settings()
		self.initialize_hard_settings()

		#Speed up scale for points
		self.score_scale = 1.1

	def initialize_dynamic_settings(self):
		self.alien_speed = 1.0
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.fleet_direction = 1
		#Points for aliens
		self.alien_point = 50

	def initialize_normal_settings(self):
		#Normal mode settings for normal button
		self.alien_speed = 1.5
		self.ship_speed = 2.0
		self.bullet_speed = 3.5
		self.fleet_direction = 1
		#Points for aliens
		self.alien_point = 60

	def initialize_hard_settings(self):
		#Hard mode settings for normal button
		self.alien_speed = 2.0
		self.ship_speed = 2.5
		self.bullet_speed = 4.0
		self.fleet_direction = 1
		#Points for aliens
		self.alien_point = 70


	def increase_speed(self):
		self.alien_speed *= self.speed_scale
		self.ship_speed *= self.speed_scale
		self.bullet_speed *= self.speed_scale

		self.alien_point = int(self.alien_point * self.score_scale)

	def get_new_ship_type(self):
		"""Get a random number to change ship type"""
		ship_types = self.ship_type
		self.random = randint(1,ship_types)


	def update_new_ship(self):
		"""Enhanced ship new atributtes"""
		if self.random == 1:
			self.ship_speed = 2.0
			self.bullet_speed = 4.0
			self.bullet_width = 10
			self.bullet_color = (255, 255,0 )
		elif self.random == 2:
			self.ship_speed = 2.0
			self.bullet_speed = 4.0
			self.bullet_width = 20
			self.bullet_color = (0, 255,200 )
