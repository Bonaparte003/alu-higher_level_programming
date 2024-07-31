#!/usr/bin/python3
"""
Create class Square that inherits from Rectangle:
    1.with private attributes each with public getters
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """inheritance"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """the method used to override the __str__ method"""
        if args and len(args) != 0:
            i = 0
            for k in args:
                if i == 0 and k is not None:
                    self.id = k
                elif i == 1:
                    self.size = k
                elif i == 2:
                    self.x = k
                elif i == 3:
                    self.y = k
                i += 1
        elif kwargs and len(kwargs) != 0:
            for m, n in kwargs.items():
                if m == "id" and n is not None:
                    self.id = n
                elif m == "size":
                    self.size = n
                elif m == "x":
                    self.x = n
                elif m == "y":
                    self.y = n

    def to_dictionary(self):
        """method that returns the dictionary represantation of Rect"""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }

    def __str__(self):
        """prints to stdout"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
