# Import needed modules
import random
import re
from .utilities import *

def prompt(message, allow_empty=True):
    """
    Minimal prompt replacement so code using `prompt(msg)` or `prompt(msg, False)` works.
    Returns the raw input string; if allow_empty is False and input is empty, returns an empty string.
    """
    try:
        resp = input(message)
    except Exception:
        # Fallback in environments without a standard input
        resp = ""
    if not allow_empty and resp.strip() == "":
        return ""
    return resp

def convert_to_float(value, default=0.0):
    """
    Safely convert a value to float; return `default` on empty input or conversion errors.
    Accepts numeric values or strings (with surrounding whitespace allowed).
    """
    try:
        if isinstance(value, str):
            value = value.strip()
            if value == "":
                return default
        return float(value)
    except (ValueError, TypeError):
        return default

class CoffeeShopSimulator:
    # Minimum and maximum temperatures
    Temp_Min = 20
    Temp_Max = 90

    def __init__(self, player_name, shop_name):

        # Set player and coffee shop names
        self.player_name = player_name
        self.shop_name = shop_name

        # Current day number
        self.day = 1

        #Cash on hand at start
        self.cash = 100.00

        # Inventory at start
        self.coffee_inventory = 100

        #Sales list
        self.sales = []

        # Possible temperatures
        self.temps = self.make_temp_distribution()

        def run(self):
            print("\nOk, lets get started. Have fun")

            #The main game loop
            running = True

            while running:

                # Display the day and a "fancy" text effect
                self.day_header()

                # Get the weather
                temperature = self.weather  

                # Display the cash and weather
                self.daily_stats(temperature)

                # Get price of a cup of coffee
                cup_price =  float(prompt("What do you want to charge per cup of coffee?"))

                # Get advertising spend
                print("\nYou can buy advertising to help promote sales")
                advertising = prompt("How much do you want to spend on advertising today? (0 for none)?", False)

                # Convert advertising into a float
                advertising = convert_to_float(advertising)

                # Deduct advertising from cash on hand
                self.cash -= advertising

                # Simulate todays's sales
                cups_sold = self.simulate(temperature, advertising, cup_price)
                gross_profit = cups_sold * cup_price

                # Dsiplay the results
                print("You sold " + str(cups_sold) + " cups of coffee today.")
                print("You made $" + str(gross_profit) + ".")

                # Add the profit to our coffers
                self.cash += gross_profit   

                # Subtract inventory
                self.coffee_inventory -= cups_sold

                # Before we loop around, add a day
                self.increment_day()



        def simulate(self, temperature, advertising, cup_price):
            # Find out how many cups were sold
            cups_sold = self.daily_sales(temperature, advertising)

            # Save the sales data for today
            self.sales.append({ 
                "day" : self.day,
                "coffee_inv" : self.coffee_inventory,
                "advertising" : advertising,
                "temp" : temperature,
                "cup_price" : cup_price,
                "cups_sold" : cups_sold
            })

            # We technically don't need this, but why make the next step
            # read from the sales list when we have the data right here
            return cups_sold
        
        def make_temp_distribution(self):
            # This is not a good bell curve, but it will do for now
            # Until we get to more advanced mathematics
            temps = []

            # First, find the average between Temp_Min and Temp_Max
            avg = (self.Temp_Min + self.Temp_Max) / 2
            # Find the distance between Temp_Max and the average
            max_dist_from_avg = self.Temp_Max - avg

            # loop trough all possible temperatures
            for i in range(self.Temp_Min, self.Temp_Max):
                # How far away is the temperature from average?
                # abs() gives us  the absolute value
                dist_from_avg = abs(avg - i)
                # How far is the dist_from_avg from the maximum?
                # This will be lower for temps at the extremes
                dist_from_max = max_dist_from_avg - dist_from_avg
                # If the value is zero, make it one
                if dist_from_max == 0:
                    dist_from_max = 1
                # Append the ouput of x_ of_y to the temps 
                for t in x_of_y(int(dist_from_max), i):
                    temps.append(t)

            return temps
        
        def increment_day(self):
            self.day += 1

        def daily_stats(self, temperature):
            print("You have $" + str(self.cash) + " cash on hand and the temperature is " + str(temperature + "."))
            print("You have enough coffee on hand to make " + str(self.coffee_inventory) + " cups \n")

        def day_header(self):
            print("\n-----| Day " + str(self.day) + "@" + self.shop_name + " |-----\n")

        def daily_sales(self, temperature, advertising):
            return int((self.Temp_Max - temperature) * (advertising * 0.5))
        
        @property
        def weather(self):
            # Generate a random temperature between 20 and 90
            # We'll consider seasons later on, but this is good enough for now
            return random.choice(self.temps)