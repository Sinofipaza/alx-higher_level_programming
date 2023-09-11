#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(Rectangle):
    """ square """
    def __init__(self, size):
        """ initialize """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
