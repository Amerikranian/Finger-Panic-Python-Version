"""The base state object. Contains bare minimum of implementation. Those who wish to use this should inherit from the class
"""

class State:
	"""The base state class
		Parameters:
			on_change (callable): Triggered whenever the state wishes to be changed
	"""

	def __init__(self, on_change):
		self.on_change = on_change

	def enter(self):
		"""Designed to initialize the state-specific variables upon entering the state"""
		pass

	def exit(self):
		"""Designed to uninitialize the state-specific variables upon exiting the state"""
		pass

	def update(self, events, delta):
		"""Designed to update the game state
			Parameters:
				events (list): Single events which have occurred since last frame
				delta (float): The time elapsed since the last frame
		"""
		pass

