import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from background import Background
from random import randint
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
from black_hole import BlackHole


class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.stats = GameStats(self)
		self.score = ScoreBoard(self)
		self.blackholes = pygame.sprite.GroupSingle()
		self.background = Background(self)
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens =pygame.sprite.Group()

		#Create starting alien fleet
		self._create_fleet()

		#Make the play button
		self.play_button = Button(self, 'OPPRESSED')
		self.easy_button = Button(self,'American')
		self.normal_button = Button(self,'European')
		self.hard_button = Button(self,'Asian')
		
	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			self._check_events()

			if self.stats.game_active == True:
				self._update_ship()
				self._update_bullets()
				self._update_aliens()
				self._create_black_hole()
			
			self._update_screen()

			
	def _check_events(self):
		# Watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					#Write the highscore to file
					self._high_score_file() 
					sys.exit()

				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_position = pygame.mouse.get_pos()
					self._check_play_button(mouse_position)

				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
						
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

	def _check_play_button(self, mouse_position):
		"""Start a new game when the player clicks a button."""
		button_clicked = self.play_button.rect.collidepoint(mouse_position)
		easy_button_clicked = self.easy_button.rect.collidepoint(mouse_position)
		normal_button_clicked = self.normal_button.rect.collidepoint(mouse_position)
		hard_button_clicked = self.hard_button.rect.collidepoint(mouse_position)
		
		if (button_clicked or easy_button_clicked) and not self.stats.game_active:
			#Reset the game settings
			self.settings.initialize_dynamic_settings()
			#Reset game statistics
			self.stats.reset_stats()
			self.stats.game_active = True
			self.score.prep_score()
			self.score.prep_level()
			self.score.prep_ships()

			#Clear bullets and aliens
			self.bullets.empty()
			self.aliens.empty()

			#Create aliens fleet and center the ship
			self._create_fleet()
			self.ship.center_ship()

			#Hide the mouse coursor
			pygame.mouse.set_visible(False)

		elif normal_button_clicked and not self.stats.game_active :
			#Reset the game settings
			self.settings.initialize_normal_settings()
			#Reset game statistics
			self.stats.reset_stats()
			self.stats.game_active = True
			self.score.prep_score()
			self.score.prep_level()
			self.score.prep_ships()

			#Clear bullets and aliens
			self.bullets.empty()
			self.aliens.empty()

			#Create aliens fleet and center the ship
			self._create_fleet()
			self.ship.center_ship()

			#Hide the mouse coursor
			pygame.mouse.set_visible(False)

		elif hard_button_clicked and not self.stats.game_active:
			#Reset the game settings
			self.settings.initialize_hard_settings()
			#Reset game statistics
			self.stats.reset_stats()
			self.stats.game_active = True
			self.score.prep_score()
			self.score.prep_level()
			self.score.prep_ships()

			#Clear bullets and aliens
			self.bullets.empty()
			self.aliens.empty()

			#Create aliens fleet and center the ship
			self._create_fleet()
			self.ship.center_ship()

			#Hide the mouse coursor
			pygame.mouse.set_visible(False)

	def _check_keydown_events(self,event):
		"""Respond to keypresses."""
		if event.key == pygame.K_RIGHT:
			self.ship.move_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.move_left = True
		elif event.key == pygame.K_UP:
			self.ship.move_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.move_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self,event):
		"""Respond to releases."""
		if event.key == pygame.K_RIGHT:
			self.ship.move_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.move_left = False
		elif event.key == pygame.K_UP:
			self.ship.move_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.move_down = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _delete_disappeared_bullet(self):
		# Get rid of bullets that have disappeared.
			for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)

	def _create_fleet(self):
		"""Create the fleet of aliens."""
		#Make an alien
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2* alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		#Calculate how many rows of aliens can fit
		ship_height = self.ship.rect.height 
		available_space_y = self.settings.screen_height - (4 * alien_height) - ship_height
		number_rows = available_space_y // (2 * alien_height)

		#Create full fleet of aliens
		for number_row in range(number_rows):
			for alien_number in range(number_aliens_x):
				#Create a random number for each alien position
				random_number = randint(-30, 30)
				#Create an alien and place it in a row
				self._create_alien(alien_number, number_row, random_number)
 
	def _create_alien(self,alien_number, number_row, random_number):
		#Create an alien and place it in a row
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number + random_number
		alien.rect.x = alien.x
		alien.y = alien_height + 2 * alien_height *number_row + random_number
		alien.rect.y = alien.y 
		self.aliens.add(alien)
		#Alien group lengh
		self.aliens_length = len(self.aliens)

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached an edge."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction."""
		random_number = randint(-10,10)
		for alien in self.aliens.sprites():
			alien.rect.y += (self.settings.fleet_drop_speed + random_number)
		self.settings.fleet_direction *= -1


	def _update_aliens(self):
		"""
		Check if the fleet is at an edge,
		then update the positions of all aliens in the fleet.
		"""
		self._check_fleet_edges()
		self.aliens.update()
		#Look for alien-ship collision
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		#Look for aliens that reach the bottom
		self._check_aliens_bottom()

	def _update_ship(self):
		"""Update position of ship"""
		self.ship.update()
		self._check_ship_black_hole_collision()

	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""
		# Update bullet positions.
		self.bullets.update()
		self._delete_disappeared_bullet()
		self._check_bullet_alien_collision()

	def _check_bullet_alien_collision(self):
		#Check for any bullet that might hit an alien
		#If so ,delete the bullet and the alien hit
		collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()
			self.background.change_background()
			self.settings.increase_speed()
			#Increase level 
			self.stats.level += 1
			self.score.prep_level()
			sleep(0.3)

		if collisions:
			for alien in collisions.values():
				self.stats.score += self.settings.alien_point
			self.score.prep_score()
			self.score.check_high_score()
			self._high_score_file() 


	def _check_aliens_bottom(self):
		"""Check for aliens that reach the bottom of the screen"""
		self.screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= self.screen_rect.bottom:
				self._ship_hit()
				break

	def _high_score_file(self):
		""""Write the highscore to a file"""
		filename = 'highscore.txt'
		with open(filename, 'w') as file_object:
			file_object.write(str(self.stats.high_score))  


	def _ship_hit(self):
		"""Respond to the ship being hit by an alien."""
		if self.stats.ships_left > 0:
			#Decrement ships left
			self.stats.ships_left -= 1
			self.score.prep_ships()

			# Get rid of any remaining aliens and bullets.
			self.aliens.empty()
			self.bullets.empty() 

			# Create a new fleet and center the ship.
			self.ship.center_ship()
			self._create_fleet()

			#Pause
			sleep(0.5)
		else:
			self.stats.game_active = False
			#Show the mouse coursor
			pygame.mouse.set_visible(True)

	def _create_black_hole(self):
		black_hole = BlackHole(self)
		self.blackholes.add(black_hole)

	def _check_ship_black_hole_collision(self):
		"""Checks if ship hits blackhole and changes apperence"""
		for blackhole in self.blackholes.copy():
			blackhole_rect = blackhole.rect
			collide = self.ship.rect.colliderect(blackhole_rect)
			if collide and self.stats.level == 1:
				self.blackholes.remove(blackhole)
				self.background.change_background()
				self.ship.change_ship(self.settings.get_new_ship_type())
				self.settings.update_new_ship()
				


	def _update_screen(self):
		# Redraw the screen during each pass through the loop.
			self.background.blitme()
			#To color the background undo '#' in method bellow
			#self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

			for bullet in self.bullets.sprites():
				bullet.draw_bullet()

			self.aliens.draw(self.screen)

			#Draw a black hole if the alien fleet is cut half in size
			for blackhole in self.blackholes.sprites():
				if (len(self.aliens) <= self.aliens_length / 2) and (self.stats.level == 1) :
					self.blackholes.draw(self.screen)


			#Draw the score information
			self.score.show_score()

			#Draw the play button
			if not self.stats.game_active:
				self.play_button.draw_button()

			if not self.stats.game_active:
				self.easy_button.draw_button()
			self.easy_button.change_button_easy_pos()

			if not self.stats.game_active:
				self.normal_button.draw_button()
			self.normal_button.change_button_normal_pos()

			if not self.stats.game_active:
				self.hard_button.draw_button()
			self.hard_button.change_button_hard_pos()

			# Make the most recently drawn screen visible.
			pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()