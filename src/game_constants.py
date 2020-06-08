"""Contains constants used for gameplay, such as state names and sound path
	Whenever this will be imported, the name will be shortened down to gmc
"""

#Game states
STATE_EXITING = -1
STATE_MAIN_MENU = 0
STATE_PLAYING = 1

#Sound constants. Prepend goes before the sound, append goes after the filename
SOUND_PREPEND = "sounds/"
SOUND_APPEND = ".ogg"

#Movement constants
DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3

#Game-specific constants, use this if you want to adjust the game values
GRID_MAXIMUM_X = 6
GRID_MAXIMUM_Y = 6
#Used for determining if the game should end, in seconds
GAME_TOTAL_TIME = 10
#Time to subtract as the user continues finding crackerjacks, in seconds
GAME_CRACKERJACK_LOSS_TIME = 0.5
#Frequency with which time subtraction occurs, in seconds. Lower values generally equate to a quicker game
GAME_CRACKERJACK_LOSS_FREQUENCY = 10
#Amount of points to award the player when they find the crackerjack
GAME_CRACKERJACK_POINT_VALUE = 10

