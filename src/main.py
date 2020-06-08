"""The main module for the game
	Starts up and let's the app run, quitting afterwards
	Please note. This already assumes that Lucia has been initialized. It is not by choice. Lucia prevents the creation of audio subsystem before it's init function has been called
"""

import game
import game_constants as gmc
import lucia
import main_menu

class App:
	"""The main application class
		Parameters:
			window_title (str): The title of the game
			screen_size (optional, list): The size of the window
			framerate (optional, float): Game FPS
	"""

	def __init__(self, window_title, screen_size = (640, 480), framerate = 60):
		if len(screen_size) < 2:
			raise ValueError("Screen size length must be at least 2, not %d" % len(screen_size))
			self.quit()
		self.game_states = [
			main_menu.MainMenu(self.change_state),
			game.Game(self.change_state)
		]
		self.current_state = None
		self.wants_to_quit = False
		self.framerate = framerate
		self.delta = 1 / framerate
		self.game_clock = lucia.pygame.time.Clock()
		self.window_title = window_title
		self.screen_instance = None
		self.screen_size = screen_size

	def begin(self):
		"""Begins the app execution"""
		self.screen_instance = lucia.show_window(self.window_title, self.screen_size)
		self.change_state(gmc.STATE_MAIN_MENU)

	def quit(self):
		"""Cleans up resources in regards to Lucia and pygame"""
		lucia.quit()

	def change_state(self, new_state):
		"""Changes the current game state.
			Parameters:
				new_state (int): A valid index corresponding to one of the states in self.game_states. If the index is below 0 or beyond len(self.game_states), the game will attempt to exit
		"""
		if self.current_state:
			self.current_state.exit()
		if new_state < 0 or new_state > len(self.game_states) - 1:
			self.wants_to_quit = True
			return
		self.current_state = self.game_states[new_state]
		self.current_state.enter()

	def run(self):
		"""Updates the current game state"""
		while not self.wants_to_quit:
			events = lucia.process_events()
			self.current_state.update(events, self.delta)
			self.game_clock.tick(self.framerate)

if __name__ == "__main__":
	my_app = App("Finger Panic")
	my_app.begin()
	my_app.run()