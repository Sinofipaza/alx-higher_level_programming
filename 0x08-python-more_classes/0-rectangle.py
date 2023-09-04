#!/usr/bin/python3
class Rectangle:
    """Empty class per task instructions"""
    pass

Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
