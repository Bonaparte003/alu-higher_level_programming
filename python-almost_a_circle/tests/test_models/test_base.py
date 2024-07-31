#!/usr/bin/python3
"""unittest for the base.py file"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation"""

    def test_no_argument(self):
        a1 = Base()
        a2 = Base()
        self.assertEqual(a1.id, a2.id - 1)

    def test_3_base(self):
        a1 = Base()
        a2 = Base()
        a3 = Base()
        self.assertEqual(a1.id, a3.id - 2)

    def test_no_id(self):
        a1 = Base(None)
        a2 = Base(None)
        self.assertEqual(a1.id, a2.id - 1)

    def test_uniqueness_id(self):
        self.assertEqual(13, Base(13).id)

    def test_nb_after_unique_id(self):
        a1 = Base()
        a2 = Base(12)
        a3 = Base()
        self.assertEqual(a1.id, a3.id - 1)

    def test_public_id(self):
        a = Base(10)
        a.id = 13
        self.assertEqual(13, a.id)

    def test_nb_private(self):
        with self.assertRaises(AttributeError):
            print(Base(13).__nb_instances)

    def test_string_id(self):
        self.assertEqual('World', Base("World").id)

    def test_floating_id(self):
        self.assertEqual(3.5, Base(3.5).id)

    def test_complx_id(self):
        self.assertEqual(complex(4), Base(complex(4)).id)

    def test_dic_id(self):
        self.assertEqual({"a": 3, "b": 5}, Base({"a": 3, "b": 5}).id)

    def test_boolean_id(self):
        self.assertEqual(False, Base(False).id)

    def test_listid(self):
        self.assertEqual([2, 3, 4], Base([2, 3, 4]).id)

    def test_tupleid(self):
        self.assertEqual((2, ), Base((2, )).id)

    def test_setid(self):
        self.assertEqual({2, 3, 4}, Base({2, 3, 4}).id)

    def test_frozensetid(self):
        self.assertEqual(frozenset({2, 4, 6}), Base(frozenset({2, 4, 6})).id)

    def test_rangeid(self):
        self.assertEqual(range(3), Base(range(3)).id)

    def test_bytesid(self):
        self.assertEqual(b'Bytes', Base(b'Bytes').id)

    def test_bytearrayid(self):
        self.assertEqual(bytearray(b'abc'), Base(bytearray(b'abc')).id)

    def test_memoryviewid(self):
        self.assertEqual(memoryview(b'abc'), Base(memoryview(b'abc')).id)

    def test_infid(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaNid(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_arguments(self):
        with self.assertRaises(TypeError):
            Base(2, 3)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string"""

    def test_to_json_string_rect_type(self):
        rec = Rectangle(1, 7, 4, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rec.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        rec = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rec.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_twodict(self):
        rec1 = Rectangle(2, 3, 5, 19, 2)
        rec2 = Rectangle(4, 2, 4, 1, 12)
        list_d = [rec1.to_dictionary(), rec2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_d)) == 106)

    def test_to_json_string_sq_type(self):
        sq = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_sq_one_dict(self):
        sq1 = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([sq1.to_dictionary()])) == 39)

    def test_to_json_string_square_two_d(self):
        sq1 = Square(10, 2, 3, 4)
        sq2 = Square(4, 5, 21, 2)
        list_d = [sq1.to_dictionary(), sq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_d)) == 78)

    def test_to_json_string_empty_l(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_str_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_str_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_file(unittest.TestCase):
    """Unittests for testing save_to_file"""

    @classmethod
    def tearDown(self):
        """Delete made files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rect(self):
        rec = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r") as rr:
            self.assertTrue(len(rr.read()) == 53)

    def test_save_to_file_two_rects(self):
        rec1 = Rectangle(10, 7, 2, 8, 5)
        rec2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r") as rr:
            self.assertTrue(len(rr.read()) == 105)

    def test_save_to_file_one_sq(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as rr:
            self.assertTrue(len(rr.read()) == 39)

    def test_save_to_file_two_sqs(self):
        sq1 = Square(10, 7, 2, 8)
        sq2 = Square(8, 1, 2, 3)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as rr:
            self.assertTrue(len(rr.read()) == 77)

    def test_save_to_file_cls_name_filenames(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file([sq])
        with open("Base.json", "r") as rr:
            self.assertTrue(len(rr.read()) == 39)

    def test_save_to_file_overwriting(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as rr:
            self.assertTrue(len(rr.read()) == 39)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as rr:
            self.assertEqual("[]", rr.read())

    def test_save_to_file_empty_l(self):
        Square.save_to_file([])
        with open("Square.json", "r") as rr:
            self.assertEqual("[]", rr.read())

    def test_save_to_file_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_argument(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """testing for from_json_string"""

    def test_from_json_string_types(self):
        list_in = [{"id": 89, "width": 10, "height": 4}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list, type(list_out))

    def test_from_json_stri_one_rectangle(self):
        list_in = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_str_two_rectangles(self):
        list_in = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_one_sq(self):
        list_in = [{"id": 89, "size": 10, "height": 4}]
        json_list_in = Square.to_json_string(list_in)
        list_out = Square.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_two_sqs(self):
        list_in = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_in = Square.to_json_string(list_in)
        list_out = Square.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_l(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """testing create method of Base class"""

    def test_create_rectangle_org(self):
        rec1 = Rectangle(3, 5, 1, 2, 7)
        r1_d = rec1.to_dictionary()
        rec2 = Rectangle.create(**r1_d)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec1))

    def test_create_rec_new(self):
        rec1 = Rectangle(3, 5, 1, 2, 7)
        r1_d = rec1.to_dictionary()
        rec2 = Rectangle.create(**r1_d)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec2))

    def test_create_rec_is(self):
        rec1 = Rectangle(3, 5, 1, 2, 7)
        r1_d = rec1.to_dictionary()
        rec2 = Rectangle.create(**r1_d)
        self.assertIsNot(rec1, rec2)

    def test_create_rec_equals(self):
        rec1 = Rectangle(3, 5, 1, 2, 7)
        r1_d = rec1.to_dictionary()
        rec2 = Rectangle.create(**r1_d)
        self.assertNotEqual(rec1, rec2)

    def test_create_square_org(self):
        sq1 = Square(3, 5, 1, 7)
        s1_d = sq1.to_dictionary()
        sq2 = Square.create(**s1_d)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq1))

    def test_create_sq_new(self):
        sq1 = Square(3, 5, 1, 7)
        s1_d = sq1.to_dictionary()
        sq2 = Square.create(**s1_d)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq2))

    def test_create_sq_is(self):
        sq1 = Square(3, 5, 1, 7)
        s1_d = sq1.to_dictionary()
        sq2 = Square.create(**s1_d)
        self.assertIsNot(sq1, sq2)

    def test_create_sq_equals(self):
        sq1 = Square(3, 5, 1, 7)
        s1_d = sq1.to_dictionary()
        sq2 = Square.create(**s1_d)
        self.assertNotEqual(sq1, sq2)


class TestBase_load_from_file(unittest.TestCase):
    """testing load_from_file_method for Base class"""

    @classmethod
    def tearDown(self):
        """delete made files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_files_first_rectangle(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rec1, rec2])
        list_rectangles_out = Rectangle.load_from_file()
        self.assertEqual(str(rec1), str(list_rectangles_out[0]))

    def test_load_from_file_second_rec(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rec1, rec2])
        list_rectangles_out = Rectangle.load_from_file()
        self.assertEqual(str(rec2), str(list_rectangles_out[1]))

    def test_load_from_file_rectangle_typ(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rec1, rec2])
        out = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in out))

    def test_load_from_file_first_sq(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        list_squares_out = Square.load_from_file()
        self.assertEqual(str(sq1), str(list_squares_out[0]))

    def test_load_from_file_second_sq(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        list_squares_out = Square.load_from_file()
        self.assertEqual(str(sq2), str(list_squares_out[1]))

    def test_load_from_file_square_typ(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        out = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in out))

    def test_load_from_file_no_files(self):
        out = Square.load_from_file()
        self.assertEqual([], out)

    def test_load_from_file_more_than_one_argument(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


'''class TestBase_save_to_file_csv(unittest.TestCase):
    """testing save_to_file_csv method of Base class"""

    @classmethod
    def tearDown(self):
        """Delete any made files"""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rec(self):
        rec = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rec])
        with open("Rectangle.csv", "r") as rr:
            self.assertTrue("5,10,7,2,8", rr.read())

    def test_save_to_file_csv_two_rec(self):
        rec1 = Rectangle(10, 7, 2, 8, 5)
        rec2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rec1, rec2])
        with open("Rectangle.csv", "r") as rr:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", rr.read())

    def test_save_to_file_csv_one_sq(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as rr:
            self.assertTrue("8,10,7,2", rr.read())

    def test_save_to_file_csv_two_sq(self):
        sq1 = Square(10, 7, 2, 8)
        sq2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        with open("Square.csv", "r") as rr:
            self.assertTrue("8,10,7,2\n3,8,1,2", rr.read())

    def test_save_to_file__csv_clsname(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file_csv([sq])
        with open("Base.csv", "r") as rr:
            self.assertTrue("8,10,7,2", rr.read())

    def test_save_to_file_csv_overwriting(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file_csv([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as rr:
            self.assertTrue("8,10,7,2", rr.read())

    def test_save_to_file__csv_none(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as rr:
            self.assertEqual("[]", rr.read())

    def test_save_to_file_csv_empty_l(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as rr:
            self.assertEqual("[]", rr.read())

    def test_save_to_file_csv_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_argument(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_fromfile_csv(unittest.TestCase):
    """testing load_from_file_csv of Base class"""

    @classmethod
    def tearDown(self):
        """Delete made files"""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rect(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec1, rec2])
        list_rectangles_out = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec1), str(list_rectangles_out[0]))

    def test_load_from_file_csv_2nd_rectangle(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec1, rec2])
        list_rectangles_out = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec2), str(list_rectangles_out[1]))

    def test_load_from_file_csv_rectangle_typ(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec1, rec2])
        out = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in out))

    def test_load_from_file_csv_first_sq(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        list_squares_out = Square.load_from_file_csv()
        self.assertEqual(str(sq1), str(list_squares_out[0]))

    def test_load_from_file_csv_second_sq(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        list_squares_out = Square.load_from_file_csv()
        self.assertEqual(str(sq2), str(list_squares_out[1]))

    def test_load_from_file_csv_square_typ(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        out = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in out))

    def test_load_from_file_csv_no_files(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], out)

    def test_load_from_file_csv_more_than_one_argument(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)'''


if __name__ == "__main__":
    unittest.main()
