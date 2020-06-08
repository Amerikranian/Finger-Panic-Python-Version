"""The main menu of the game
	This is a bare bones implementation of an audiogame menu, only containing support for spoken items
	More functionality may be added as the project grows
"""

import game_constants as gmc
import game_globals as glb
import lucia
import state


class MainMenu(state.State):
	"""The main menu of the game
		Options are direct sound paths to the items being played
		Parameters:
			on_change (callable): See State docstring
	"""

	def __init__(self, on_change):
		super().__init__(on_change)
		self.options = [
			"menu/start game",
			"menu/exit"
		]
		self.menu_index = -1
		self.menu_music = "menu/background"
		#Since we don't have a dedicated enter sound, we'll use the edge sound as confirmation
		self.enter_sound = "menu/atedge"
		self.music_slot = None

	def enter(self):
		"""Begins the menu execution"""
		self.music_slot = glb.play_sound(self.menu_music, 0, True)

	def exit(self):
		"""Finishes the menu execution"""
		glb.destroy_sound(self.music_slot)

	def run_internals(self):
		"""Outputs the current item to the user. Can be expanded with different item types and or recognition that some items may be disabled.
			This function should not be ran directly, as the only usefulness it possesses is contained in the soul fact that it reacts to the menu being changed
		"""
		glb.play_sound(self.options[self.menu_index])

	def change_index(self, value):
		"""Updates and fixes the menu index as requested by the user
			Parameters:
				value (int): The adjustment of the menu index, typically 1 or -1.
		"""
		self.menu_index += value
		#Todo: Possibly adding ability to toggle wrapping
		if self.menu_index < 0:
			self.menu_index = len(self.options) - 1
		elif self.menu_index >= len(self.options):
			self.menu_index = 0
		self.run_internals()

	def process_choice(self):
		"""Processes the user's menu selection
			This function should not be called directly
		"""
		#Todo: Perhaps separate sound logic and availibility of choices into a different function
		glb.play_sound(self.enter_sound)
		if self.menu_index == 0:
			self.on_change(gmc.STATE_PLAYING)
		else:
			self.on_change(gmc.STATE_EXITING)


	def update(self, events, delta):
		"""Processes user input and changes state based on the chosen option
			Parameters:
				events (list): Single events occurred since last frame
				delta (float): Time elapsed since last frame
		"""
		for event in events:
			if event.type == lucia.KEYDOWN:
				if event.key == lucia.K_UP:
					self.change_index(-1)
					break
				elif event.key == lucia.K_DOWN:
					self.change_index(1)
					break
				elif event.key == lucia.K_RETURN:
					self.process_choice()