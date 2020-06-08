"""The grid used for game purposes
"""

import random

class Grid:
	"""The base grid class
		Parameters:
			max_x (int): Maximum x of the grid
			max_y (int): Maximum y of the grid
	"""

	def __init__(self, max_x, max_y):
		self.maximum_x = 0
		self.maximum_y = 0
		self.tiles = []
		#Will be used as the surface of the grid
		#Possibly change later to support different surfaces and boarders?
		self.grid_surface = "move"
		self.boarder_surface = "atedge"
		self.resize_self(max_x, max_y)

	def __getitem__(self, key):
		"""Allows the bracket notation for the grid
			Parameters:
				key (int): The index of the row one wishes to access
			Return Value:
				The requested row of the grid.
		"""
		return self.tiles[key]

	def resize_self(self, max_x, max_y):
		"""Resizes the grid based on the given parameters
			Parameters:
				max_x (int): See class docstring
				max_y (int): See class docstring
		"""
		self.maximum_x = max_x
		self.maximum_y = max_y
		self.tiles = [[0 for y in range(max_y)]for x in range(max_x)]

	def get_surface(self, x, y):
		"""Retrieves the surface of the grid
			Parameters:
				x (unused, int): The x coordinate at which one wishes to retrieve a tile from the grid
				y (unused, int): The y coordinate at which one wishes to retrieve a tile from the grid
		"""
		return self.grid_surface

	def spawn_crackerjack(self, x, y):
		"""Spawns a crackerjack excluding the provided coordinates
			Since the game is so simplistic right now, a simple value of 1 will replace one of the zeros in the list.
			One may wish to write a basic crackerjack class should they choose to have multiple objects on the board.
			Parameters:
				x (int): Excluded x coordinate
				y (int): Excluded y coordinate
		"""
		temp_x = 0
		temp_y = 0
		while True:
			temp_x = random.randint(0, self.maximum_x - 1)
			temp_y = random.randint(0, self.maximum_y - 1)
			if temp_x == x or temp_y == y:
				continue
			break
		self.tiles[temp_x][temp_y] = 1

