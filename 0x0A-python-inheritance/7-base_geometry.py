#!/usrbin/python3
"""Imports module here """


class BaseGeometry:
    """an empty class """
    def area(self):
        """raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates inputs
        Args:
            name: a string to be checked
            value: must be greater than 0
        Raises:
            TypeError: must be an integer
            ValueError: Must be Greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
