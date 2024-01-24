#!/usr/bin/python3
"""defention for square module"""


class Square:
    """define square"""

    def __init__(self, size=0):
        """Intiant a square object

        Args:
            size: the integer length of square side
        """
        self.__size = size

    def area(self):
        """calc the area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
