class GameStats():
	"""A class to manage the stats of game"""
	def __init__(self,ai_game):
		self.settings = ai_game.settings
		#High score should never be reset
		filename = 'highscore.txt'
		with open(filename) as f:
			for line in f:
				high_score = line
		self.high_score = int(high_score)

		self.reset_stats()
		#Flag to decide if game continues
		self.game_active = False


	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ships_limit
		self.score = 0
		self.level = 1