#!/usr/bin/python3
""" User_class"""

class User():
    """Documents."""

    def __init__(self):
        """Documents. """
        self.__email = None

    @email.setter
    def email(self, value):
        """ Documents."""
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    @property
    def email(self):
        """Documents."""
        return self.__email
   
    
if __name__ == "__main__":

    u = User()
    u.email = "shametlab@gmail.com"
    print(u.email)
