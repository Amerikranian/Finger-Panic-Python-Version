"""A basic item class for the menu"""

class MenuItem:
	"""A basic menu item class
		Parameters:
			item_name (str): The name of the item, will be seen as the user scrolls through the menu
			item_type (MENU_): one of the flags from menu_constants file
	"""

	def __init__(self, item_name, item_type):
		self.name = item_name
		self.type = item_type

