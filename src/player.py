"""The player class
	This module holds information regarding the player. This includes but is not limited to current score, current coordinates, and current level
"""

import game_constants as gmc

class Player:
	"""The player class
		Parameters:
			x (optional, int): The starting coordinate of the player
			y (optional, int): The starting y of the player
	"""

	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
		self.temp_x = 0
		self.temp_y = 0
		self.found_crackerjacks = 0
		#Used to prevent the modulous division from leveling up the player
		#Without this, whenever the player is exactly at an equal amount of GAME_CRACKERJACK_LOSS_FREQUENCY, they would continue leveling
		#Todo: Possibly replace this with a more cleaner method?
		self.last_crackerjack_value = 0
		self.score = 0
		self.level = 1

	def move(self, direction):
		"""Moves the player in a specified direction
			Parameters:
				direction (DIR): One of the dir_constants
		"""
		self.temp_x = self.x
		self.temp_y = self.y
		if direction == gmc.DIR_UP:
			self.y += 1
		elif direction == gmc.DIR_RIGHT:
			self.x += 1
		elif direction == gmc.DIR_DOWN:
			self.y -= 1
		elif direction == gmc.DIR_LEFT:
			self.x -= 1

	def reverse_self(self):
		"""Resets the player to their previous coordinates"""
		self.x = self.temp_x
		self.y = self.temp_y

