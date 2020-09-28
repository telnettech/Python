import random


Class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key value)


class Thief(Character):  # Thief class inherits Character class attributes
    sneaky = True

    # Methods defined for a class

    def pickpocket(self):
        return self.sneaky and bool(random.ranint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)


# Declares a variable that calls the class
kenneth = Thief()
# Prints the value of variable's attribute called sneaky
print(kenneth.sneaky)
