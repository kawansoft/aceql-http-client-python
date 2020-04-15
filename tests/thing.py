class Thing(object):
    def __init__(self, name, firstname, age):
        self.name = name
        self.firstname = firstname
        self.age = age

    def __str__(self):
        """ The string representation."""
        return str(self.name) + ", " + str(self.firstname) + ", " + str(self.age)
