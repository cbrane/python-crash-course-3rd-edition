"""A class that can be used to manage info about users and admins."""

# 9-8. Privliges

# 1. Write a separate Privilges class, should have one attribute, privilges,
#    that stores a list of strings just like in 9-7
# 2. Move the show_privilges() method to this class, make a Privilges instance
#    as an attribute in the Admin class, create a new instance of Admin & use
#    your method to show its privilges

class User:
    """A simple attempt to model a user."""

    def __init__(self, username, first_name, last_name, age): 
        """Initialize first and last name attributes."""
        self.username = username
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUsername: {self.username}")
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Age: {self.age}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hi {self.first_name.title()}, it is very nice to see you.")