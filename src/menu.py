"""The base menu module
	Provides the ability to create both spoken and sound menus
	More functionality may be added in the future
"""

import game_globals as glb
import lucia
import menu_constants as men_c
import menu_item
import state
from lucia import output as out

class Menu(state.State):
	"""The base menu class
		Please note. Everything following on_change must be written as name = value, i.e, menu_music = "menu/background"
		Parameters:
			options (dict): A dictionary containing menu options as it's keys and their type as it's values
			on_change (callable): A function to be called in order to resolve the user's decision. Please note: The function *must* accept one argument, the user's choice
			menu_music (str): The background music of the menu
			enter_sound: The sound heard when the user presses their enter key to quit the menu
			item_prepend (str): Only takes effect if an item is a sound, adds a path to the said item. I.e, if the prepend is "menu", the script will try to play menu/item_name. As of the current writing, this is true of all the sounds the menu plays
	"""

	def __init__(self, options, on_change, **kwargs):
		super().__init__(on_change)
		self.options = []
		self.enter_sound = kwargs.get("enter_sound", "")
		self.menu_index = -1
		self.menu_music = kwargs.get("menu_music", "")
		self.music_slot = None
		self.item_prepend = kwargs.get("item_prepend", "")
		if self.item_prepend and not self.item_prepend.endswith("/"):
			self.item_prepend += "/"
		self.reset_menu_options(options)

	def reset_menu_options(self, options):
		"""Overrides any present options within the menu with the ones given
			Parameters:
				options (dict): See class docstring
		"""
		self.options = [menu_item.MenuItem(key, options[key]) for key in options]

	def enter(self):
		"""Begins the menu execution"""
		if self.menu_music:
			self.music_slot = glb.play_sound(self.item_prepend + self.menu_music, 0, True)
		self.menu_index = -1

	def exit(self):
		"""Finishes the menu execution"""
		if self.music_slot:
			glb.destroy_sound(self.music_slot)

	def run_internals(self):
		"""Outputs the current item to the user. Can be expanded with different item types and or recognition that some items may be disabled.
			This function should not be ran directly, as the only usefulness it possesses is contained in the soul fact that it reacts to the menu being changed
		"""
		current_item = self.options[self.menu_index]
		if  current_item.type == men_c.MENU_ITEM_TTS:
			out.output(current_item.name)
		elif current_item.type == men_c.MENU_ITEM_SOUND:
			glb.play_sound(self.item_prepend + current_item.name)

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
		glb.play_sound(self.item_prepend + self.enter_sound)
		#Todo: Allow the user to mark items to take the to the same state without needing to specify each and every single choice
		#I.e, allow the user to pass in a key called "default" and trigger it if a choice doesn't exist
		self.on_change(self.menu_index)

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

