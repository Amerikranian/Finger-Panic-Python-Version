"""The main game module
	This module hosts and controls the main portion of the game
"""

import clock
import game_constants as gmc
import game_globals as glb
import grid
import lucia
import player
import state

class Game(state.State):
	"""The base game class
		Parameters:
			on_change (callable): See State docstring
	"""

	def __init__(self, on_change):
		super().__init__(on_change)
		#Used when player finds a crackerjack
		self.found_sound = "found"
		self.game_timer = clock.Clock()
		self.game_time = gmc.GAME_TOTAL_TIME
		self.grid = grid.Grid(gmc.GRID_MAXIMUM_X, gmc.GRID_MAXIMUM_Y)
		#Used when the game becomes faster
		self.level_sound = "nextlevel"
		self.music_path = "background"
		self.music_slot = None
		self.player = player.Player()

	def enter(self):
		"""Begins game execution"""
		self.music_slot = glb.play_sound(self.music_path, 0, True)
		#Since we don't have a crackerjack on the grid, we'll spawn one as the game starts
		#The grid doesn't do this on it's own because if one wishes to add different modes of gameplay, having a crackerjack on the board at the start may not be what one desires
		self.grid.spawn_crackerjack(self.player.x, self.player.y)

	def exit(self):
		"""Cleans up any resources left over after the game is finished"""
		glb.destroy_sound(self.music_slot)

	def update_player_state(self, direction):
		"""Updates the player state and fixes any values which happen to be out of range
			Parameters:
				value (DIR): See player.move docstring
		"""
		self.player.move(direction)
		#Todo: Possibly convert this into a method of player class?
		if self.player.x < 0 or self.player.x >= self.grid.maximum_x or self.player.y < 0 or self.player.y >= self.grid.maximum_y:
			glb.play_sound(self.grid.boarder_surface)
			self.player.reverse_self()
			return
		glb.play_sound(self.grid.get_surface(self.player.x, self.player.y))
		self.update_crackerjack_state()

	def update_crackerjack_state(self):
		"""Updates crackerjack-related data, such as checking if the player has found one and if so, spawning it somewhere else		"""
		if self.grid[self.player.x][self.player.y]:
			#We found a crackerjack, so let's reset the spot and play the associated fanfare
			self.game_timer.reset()
			self.grid[self.player.x][self.player.y] = 0
			glb.play_sound(self.found_sound)
			self.player.found_crackerjacks += 1
			self.player.score += gmc.GAME_CRACKERJACK_POINT_VALUE
			self.grid.spawn_crackerjack(self.player.x, self.player.y)
		if self.player.found_crackerjacks != self.player.last_crackerjack_value:
			self.check_level_conditions()

	def check_level_conditions(self):
		"""Performs and executes (if aplicable) checks to speed up the game"""
		if self.player.found_crackerjacks % gmc.GAME_CRACKERJACK_LOSS_FREQUENCY == 0:
			#We leveled!
			self.player.last_crackerjack_value = self.player.found_crackerjacks
			self.player.level += 1
			glb.play_sound(self.level_sound)
			#We ensure that the user has at least 1 second to hammer their keys in the vain hopes of finding their goal
			self.game_time = max(1, self.game_time - gmc.GAME_CRACKERJACK_LOSS_TIME)
		#Todo: Expand game leveling conditions.
		#Perhaps make the board expand?

	def update(self, events, delta):
		"""Processes user input and continues the gameplay
			Parameters:
				events (list): Single events occurred since last frame
				delta (float): Time elapsed since last frame
		"""
		#Update the game timer
		self.game_timer.tick(delta)
		#Todo: Move into separate function should logic for the game become more complex
		if self.game_timer.elapsed >= self.game_time:
			#Todo: Add a way to alert the user of their performance besides printing it
			#Todo: Return the user to the main menu from the alert
			print("Crackerjacks found: %d.\nPlayer score: %d.\nPlayer level: %d.\nTime window for finding crackerjack: %.1f seconds." % (self.player.found_crackerjacks, self.player.score, self.player.level, self.game_time))
			self.on_change(gmc.STATE_EXITING)
		for event in events:
			if event.type == lucia.KEYDOWN:
				if event.key == lucia.K_UP:
					self.update_player_state(gmc.DIR_UP)
					break
				if event.key == lucia.K_RIGHT:
					self.update_player_state(gmc.DIR_RIGHT)
					break
				if event.key == lucia.K_DOWN:
					self.update_player_state(gmc.DIR_DOWN)
					break
				if event.key == lucia.K_LEFT:
					self.update_player_state(gmc.DIR_LEFT)
					break
