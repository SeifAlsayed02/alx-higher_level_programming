#!/usr/bin/python3
"""defention for square module"""


class Square:
    """define square"""

    def __init__(self, size):
        """Intiant a square object

        Args:
            size: the integer length of square side
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calc the area of square"""

        return self.__size ** 2
