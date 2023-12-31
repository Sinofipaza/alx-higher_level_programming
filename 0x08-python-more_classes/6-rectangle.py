#!/usr/bin/python3
class Rectangle:
    """
    Create Rectangle class
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize variables
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        returns width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        returns height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets width value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        method to get area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        method to get perimeter
        """
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        print rectangle using #
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            string += "\n"
            return
        for i in range(self.__height):
            string += "#" * self.__width + "\n"
        return string[:-1]

    def __repr__(self):
        """
        print string representing width and height of rectangle
        """
        string = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return string

    def __del__(self):
        """
        deletes rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
