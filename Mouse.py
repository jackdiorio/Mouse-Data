# Define mouse class
class Mouse():

    # Class constructor
    def __init__(self, name, birthday):

        # A mouse has a name and birthday
        self.name = name
        self.birthday = birthday

    # Returns the name field
    def get_name(self):
        return self.name

# Jeff is born
jeff_the_mouse = Mouse("jeff", "1/22/2024")

# We confirm it is Jeff
print("My name is " + jeff_the_mouse.get_name())