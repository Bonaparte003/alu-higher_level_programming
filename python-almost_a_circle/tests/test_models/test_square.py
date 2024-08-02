#!/usr/bin/python3
import unittest
import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestSquareMethods(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_new_square(self):
        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_2(self):
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_squares(self):
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        new = Square(1)
        self.assertEqual(True, isinstance(new, Base))

    def test_is_Rectangle_instance(self):
        new = Square(1)
        self.assertEqual(True, isinstance(new, Rectangle))

    def test_incorrect_amount_attrs(self):
        with self.assertRaises(TypeError):
            new = Square()

    def test_incorrect_amount_attrs_1(self):
        with self.assertRaises(TypeError):
            new = Square(1, 1, 1, 1, 1)

    def test_access_private_attrs(self):
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2)

    def test_valide_attrs_2(self):
        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2)

    def test_valide_attrs_3(self):
        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2)

    def test_value_attrs(self):
        with self.assertRaises(ValueError):
            new = Square(0)

    def test_value_attrs_2(self):
        with self.assertRaises(ValueError):
            new = Square(1, -1)

    def test_value_attrs_3(self):
        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_area(self):
        new = Square(4)
        self.assertEqual(new.area(), 16)

    def test_load_from_file(self):
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_area_2(self):
        new = Square(2)
        self.assertEqual(new.area(), 4)
        new.size = 5
        self.assertEqual(new.area(), 25)

    def test_display(self):
        r1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        r1 = Square(4)
        res = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.size = 5
        res = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        r1 = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        r1 = Square(3, 2, 5, 3)
        res = "[Square] (3) 2/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.size = 11
        res = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        s1 = Square(5)
        res = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s2 = Square(3, 7, 1)
        res = "[Square] (2) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), res)

        s3 = Square(1, 1, 1)
        res = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3"
        self.assertEqual(s1.__str__(), res)

    def test_display_3(self):
        s1 = Square(5, 2, 1)
        res = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        s1 = Square(3)
        res = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

        s1.x = 1
        res = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

        s1.y = 2
        res = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_update(self):
        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_2(self):
        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_3(self):
        s1 = Square(1)
        res = "[Square] (1) 0/0 - 1\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(2, 2, 2, 2)
        res = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(x=1, size=2, id=89, y=3)
        res = "[Square] (89) 1/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_create(self):
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)

    def test_create_2(self):
        s1 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

    def test_create_3(self):
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_create_4(self):
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_save_to_file(self):
        s1 = Square(1)
        s2 = Square(2)
        l = [s1, s2]
        Square.save_to_file(l)
        res = '[{"id": 1, "size": 1, "x": 0, "y": 0}, {"id": 2, "size": 2, "x": 0, "y": 0}]'

        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_save_to_file_2(self):
        l = []
        Square.save_to_file(l)
        res = '[]'

        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_save_to_file_3(self):
        Square.save_to_file(None)
        res = '[]'

        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_2(self):
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_size_3(self):
        with self.assertRaises(TypeError):
            s1 = Square("2")

    def test_size_4(self):
        with self.assertRaises(ValueError):
            s1 = Square(2)
            s1.size = -5

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        res = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1.to_dictionary(), res)

    def test_to_dictionary_2(self):
        s1 = Square(10, 2, 1)
        res = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1.to_dictionary(), res)
        self.assertEqual(type(s1.to_dictionary()), dict)

    def test_to_dictionary_3(self):
        s1 = Square(1)
        res = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        self.assertEqual(s1.to_dictionary(), res)
