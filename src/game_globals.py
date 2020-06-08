"""Contains objects that must be accessed by multiple modules, primarily sound pool
	Please note: This initializes lucia. See docstring in main.py for an explanation as to why
	Whenever this will be imported, the name will be shortened to glb
"""

import game_constants as gmc
import lucia

lucia.initialize()

sound_pool = lucia.audio_backend.SoundPool()

def play_sound(filename, volume = 0, looping = False):
	"""A wrapper over playing functions taking into account SOUND_PREPEND and SOUND_APPEND constants
		Parameters:
			filename (str): The filename which one wishes to play
			volume (optional, float): The volume of the sound
			looping (optional, bool): Determines whether the sound loops
	"""
	return sound_pool.play_stationary_extended(gmc.SOUND_PREPEND + filename + gmc.SOUND_APPEND, looping, 0, 0, volume, 100, False)

def destroy_sound(sound):
	"""A wrapper over sound_pool.destroy_sound function"""
	sound_pool.destroy_sound(sound)