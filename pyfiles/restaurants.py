"""A class that can be used to represent a restaurant."""

class Restaurant:
    """Stores and describes info about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type): 
        """Initialize name and age attributes."""
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant that was created."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Print a message saying that the restaurant is open."""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, number):
        """Set the number of people who have been served by the restaurant."""
        self.number_served = number
    
    def increment_number_served(self, number):
        """Increment the amount of people who have been served."""
        self.number_served += number