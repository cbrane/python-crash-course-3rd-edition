"""Classes that can used to manage admins and privilges."""
from users import User

class Privileges:
    """An attempt to model privileges for an admin."""
    def __init__(self, *privileges):
        """Initialize the privileges' attributes."""
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(privilege.title())


class Admin(User):
    """A simple attempt to model an admin."""

    def __init__(self, username, first_name, last_name, age, *privileges):
        """
        Initialize attributes for the super class.
        Initialize attributes for the subclass.
        """
        super().__init__(username, first_name, last_name, age)
        self.privileges = Privileges(*privileges)