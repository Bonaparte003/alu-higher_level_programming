#!/usr/bin/python3
"""
Create class Rectangle that inherits from Base:
    1.with private attributes each with public getters
"""


from collections import OrderedDict
from models.base import Base


class Rectangle(Base):
    """inheritance"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """performs area operation"""
        return self.width * self.height

    def display(self):
        """method that prints '#' to stdout"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.__y):
            print()
        for a in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """the method used to override the __str__ method"""
        if args and len(args) != 0:
            i = 0
            for k in args:
                if i == 0 and k is not None:
                    self.id = k
                elif i == 1:
                    self.width = k
                elif i == 2:
                    self.height = k
                elif i == 3:
                    self.x = k
                elif i == 4:
                    self.y = k
                i += 1
        elif kwargs and len(kwargs) != 0:
            for m, n in kwargs.items():
                if m == "id" and n is not None:
                    self.id = n
                elif m == "width":
                    self.width = n
                elif m == "height":
                    self.height = n
                elif m == "x":
                    self.x = n
                elif m == "y":
                    self.y = n

    def to_dictionary(self):
        """method that returns the dictionary represantation of Rect"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """prints to stdout"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}"
                )
