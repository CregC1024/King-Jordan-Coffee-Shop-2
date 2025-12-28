# King Jordan's Coffee Shop Simulator 4000
# Copyright 2026 Universal Source Code LLC, All Rights Reserved.

# Written by Creg Clarence Sullivan Senior Principal Software Engineer.

# Import all functions from the utlity module
# Provide a local fallback for `prompt()` to avoid depending on an external `utilities` module.
def prompt(message, required=False):
	"""Prompt the user and optionally require non-empty input."""
	while True:
		try:
			value = input(message)
		except EOFError:
			# In non-interactive environments, return an empty string
			value = ""
		if required and not value.strip():
			print("This field is required.")
			continue
		return value

# Import the game class from the coffee_shop_simulator module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from coffee_shop_simulator import CoffeeShopSimulator  # type: ignore

try:
	from coffee_shop_simulator import CoffeeShopSimulator  # type: ignore[import]
except Exception:
	# Local fallback minimal implementation when the external module is unavailable.
	# This allows the script to run without the external dependency during development or testing.
	class CoffeeShopSimulator:
		def __init__(self, owner_name, shop_name):
			self.owner_name = owner_name
			self.shop_name = shop_name

		def run(self):
			print(f"Starting a minimal Coffee Shop Simulator for {self.owner_name} at {self.shop_name}.")
			print("Note: the real 'coffee_shop_simulator' module was not found; running fallback stub.")

#Print welcome message  
print("Welcome to King Jordan's Coffee Shop Simulator 4000")

# Get name and store
t_name = prompt("what is your name? ", True)
t_shop_name = prompt ("what do you want to name your coffee shop?", True)

# Create the game object
game = CoffeeShopSimulator(t_name, t_shop_name)

# Run the game
game.run()