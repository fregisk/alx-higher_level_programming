#!/usr/bin/python3
"""
Create a Class Square with:
- size, position private propreties
- method of area and method of print_square
- getters & setters.
"""


class Square:
    """Class - Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor of a Square with the size and position"""
        self.size = size
        self.position = position

    def area(self):
        """Method to get the area of the Square"""
        return (self.__size ** 2)

    def my_print(self):
        """Method to print a Square with spaces"""
        if (self.__size == 0):
            print()
        else:
            for blank in range(self.position[1]):
                print()
            for rows in range(self.__size):
                print(" " * self.position[0], end='')
                print("#" * self.__size)

    @property
    def size(self):
        """Getter of the private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the size private attribute"""
        if (type(value) is not int):


