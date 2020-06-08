"""A quick wrapper over adding delta and increasing time for frames (lucia timer for frames)"""

class Clock:
	"""The base Clock class
		Parameters:
			start_time (optional, float): The starting time to which the clock gets set to
	"""

	def __init__(self, start_time = 0.0):
		self.elapsed = start_time

	def reset(self):
		"""Resets the clock"""
		self.__init__()

	def set_time(self, new_time):
		"""Updates the clock time to the given time
			Parameters:
				new_time (float): The new time the clock should be set to
		"""
		self.elapsed = new_time

	def tick(self, delta):
		"""Updates the time. Must be called every frame if one wishes to have reliance.
			Parameters:
				delta (float): The increment by which the time gets updated
		"""
		self.elapsed += delta

