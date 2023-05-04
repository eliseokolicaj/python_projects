import pygame.font


class Button():
	def __init__ (self, ai_game , msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		#Set the dimensions and the property of buttom
		self.width , self.height = 200, 50
		self.button_color = (0, 0 , 50)
		self.text_color = (250, 250 , 250)
		self.font = pygame.font.SysFont(None, 46)

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0 , 0 ,self.width,self.height)
		self.rect.x = 583
		self.rect.y = 250

		# The button message needs to be prepped only once.
		self._prep_msg(msg)

	def _prep_msg(self , msg):
		"""Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(msg , True , self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)

	def change_button_easy_pos(self):
		""""Change the position of other buttons"""
		self.rect.x = 583
		self.rect.y = 350
		#change the position of the text image
		self.msg_image_rect.center = self.rect.center

	def change_button_normal_pos(self):
		""""Change the position of other buttons"""
		self.rect.x = 583
		self.rect.y = 450
		#change the position of the text image
		self.msg_image_rect.center = self.rect.center

	def change_button_hard_pos(self):
		""""Change the position of other buttons"""
		self.rect.x = 583
		self.rect.y = 550
		#change the position of the text image
		self.msg_image_rect.center = self.rect.center
		

