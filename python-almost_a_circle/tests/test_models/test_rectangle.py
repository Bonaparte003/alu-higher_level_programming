#!/usr/bin/python3
"""testing the Rectangle class"""


import sys
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiat(unittest.TestCase):
    """testing instantiation for the Rectangle class"""

    def test_rectangle_is_Base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_argumets(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_1_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_2_args(self):
        rec1 = Rectangle(10, 2)
        rec2 = Rectangle(2, 10)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_3_args(self):
        rec1 = Rectangle(2, 2, 4)
        rec2 = Rectangle(4, 4, 2)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_4_args(self):
        rec1 = Rectangle(1, 2, 3, 4)
        rec2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_5_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more__args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getting(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.width)

    def test_width_setting(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.width = 10
        self.assertEqual(10, rec.width)

    def test_height_getting(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.height)

    def test_height_setting(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_x_getting(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.x)

    def test_x_setting(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_y_getting(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.y)

    def test_y_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.y = 10
        self.assertEqual(10, rec.y)


class TestRectangle_width_cases(unittest.TestCase):
    """Unittests of Rectangle width attribute."""

    def test_no_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_string_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_floating_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complx_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dictionary_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"c": 1, "d": 2}, 2)

    '''def test_boolean_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)'''

    def test_l_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_of_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_of_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozensetwidth(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_range_with_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_with_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Bytes', 2)

    def test_bytearray_with_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview_with_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def test_inf_with_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_with_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_nega_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height_cases(unittest.TestCase):
    """Unittests for Rectangle height attribute."""

    def test_No_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_string_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_floating_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complx_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dictionary_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"b": 1, "c": 2})

    def test_l_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_with_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuples_with_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, ))

    def test_frozensetheight(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_with_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes_with_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Bytes')

    def test_bytearray_with_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryviewheight(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_nega_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_0_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x_cases(unittest.TestCase):
    """Unittests for Rectangle x attribute."""

    def test_No_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_floating_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complx_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_for_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"b": 1, "c": 2}, 2)

    '''def test_boolean_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)'''

    def test_l_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_for_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuples_for_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, ), 2)

    def test_frozensetx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_with_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_with_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearrayx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_for_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_infx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_nanx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """Unittests for Rectangle y attribute"""

    def test_No_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_floating_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complx_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_for_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_l_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_for_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuples_with_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, ))

    def test_frozensety(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_rangey(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(3))

    def test_bytesy(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Bytes')

    def test_bytearrayy(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefghi'))

    def test_memoryviewy(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfghij'))

    def test_infy(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nany(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_init(unittest.TestCase):
    """Unittests for order of attribute init"""

    def test_width_bef_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_bef_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_bef_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_bef_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_bef_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_bef_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area in Rectangle"""

    def test_areasmall(self):
        rec = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, rec.area())

    def test_arealarge(self):
        rec = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, rec.area())

    def test_area_changedattributes(self):
        rec = Rectangle(2, 10, 1, 1, 1)
        rec.width = 7
        rec.height = 14
        self.assertEqual(98, rec.area())

    def test_area_onearg(self):
        rec = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rec.area(1)


class TestRectangle_stdout_cases(unittest.TestCase):
    """Unittests for display methods of Rectangle"""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed stuffs"""

        capt = io.StringIO()
        sys.stdout = capt
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capt

    def test_str_method_print_wid_height(self):
        rec = Rectangle(4, 6)
        capt = TestRectangle_stdout_cases.capture_stdout(rec, "print")
        cor = "[Rectangle] ({}) 0/0 - 4/6\n".format(rec.id)
        self.assertEqual(cor, capt.getvalue())

    def test_str_method_wid_height_x(self):
        rec = Rectangle(5, 5, 1)
        cor = "[Rectangle] ({}) 1/0 - 5/5".format(rec.id)
        self.assertEqual(cor, rec.__str__())

    def test_str_method_wid_height_x_y(self):
        rec = Rectangle(1, 8, 2, 4)
        cor = "[Rectangle] ({}) 2/4 - 1/8".format(rec.id)
        self.assertEqual(cor, str(rec))

    def test_str_method_wid_height_x_y_id(self):
        rec = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(rec))

    def test_str_method_changing_attributes(self):
        rec = Rectangle(7, 7, 0, 0, [4])
        rec.width = 15
        rec.height = 1
        rec.x = 8
        rec.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(rec))

    def test_str_method_1_arg(self):
        rec = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rec.__str__(1)

    def test_display_wid_height(self):
        rec = Rectangle(2, 3, 0, 0, 0)
        capt = TestRectangle_stdout_cases.capture_stdout(rec, "display")
        self.assertEqual("##\n##\n##\n", capt.getvalue())

    def test_display_wid_height_x(self):
        rec = Rectangle(3, 2, 1, 0, 1)
        capt = TestRectangle_stdout_cases.capture_stdout(rec, "display")
        self.assertEqual(" ###\n ###\n", capt.getvalue())

    def test_display_wid_height_y(self):
        rec = Rectangle(4, 5, 0, 1, 0)
        capt = TestRectangle_stdout_cases.capture_stdout(rec, "display")
        disp = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(disp, capt.getvalue())

    def test_display_width_heigh_x_y(self):
        rec = Rectangle(2, 4, 3, 2, 0)
        capt = TestRectangle_stdout_cases.capture_stdout(rec, "display")
        disp = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(disp, capt.getvalue())

    def test_display_1_arg(self):
        rec = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rec.display(1)


class TestRectangle_update_arguments(unittest.TestCase):
    """Unittests for update args method of the Rectangle"""

    def test_update_arguments_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rec))

    def test_update_args_1(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rec))

    def test_update_args_2(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rec))

    def test_update_args_3(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rec))

    def test_update_args_4(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rec))

    def test_update_args_5(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rec))

    def test_update_more_than_five(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rec))

    def test_update_args_No_id(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(None)
        cor = "[Rectangle] ({}) 10/10 - 10/10".format(rec.id)
        self.assertEqual(cor, str(rec))

    def test_update_args_None_id_andmore(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(None, 4, 5, 2)
        cor = "[Rectangle] ({}) 2/10 - 4/5".format(rec.id)
        self.assertEqual(cor, str(rec))

    def test_update_arguments_twice(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4, 5, 6)
        rec.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rec))

    def test_update_args_invalid_widthtype(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(89, "invalid")

    def test_update_args_widthzero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(89, 0)

    def test_update_args_width_neg(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(89, -5)

    def test_update_args_invalid_heighttype(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(89, 2, "invalid")

    def test_update_args_height_0(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(89, 1, 0)

    def test_update_args_height_neg(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(89, 1, -5)

    def test_update_args_invalid_xtype(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(89, 2, 3, "invalid")

    def test_update_args_x_neg(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(89, 1, 2, -6)

    def test_update_args_invalidy(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_neg(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_h(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(89, "invalid", "invalid")

    def test_update_args_width_beforex(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(89, "invalid", 1, "invalid")

    def test_update_args_width_beforey(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_beforex(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(89, 1, "invalid", "invalid")

    def test_update_args_height_beforey(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_beforey(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_updatekwargs(unittest.TestCase):
    """Unittests kwargs method of the Rectangle class."""

    def test_update_kwargs_1(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rec))

    def test_update_kwargs_2(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(rec))

    def test_update_kwargs_3(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rec))

    def test_update_kwargs_4(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(rec))

    def test_update_kwargs_5(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(rec))

    def test_update_kwargs_No_id(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=None)
        cor = "[Rectangle] ({}) 10/10 - 10/10".format(rec.id)
        self.assertEqual(cor, str(rec))

    def test_update_kwargs_No_id_and_more(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=None, height=7, y=9)
        cor = "[Rectangle] ({}) 10/9 - 10/7".format(rec.id)
        self.assertEqual(cor, str(rec))

    def test_update_kwargstwice(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=89, x=1, height=2)
        rec.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(rec))

    def test_update_kwargs_invalid_widthtype(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(width="invalid")

    def test_update_kwargs_width_0(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=0)

    def test_update_kwargs_width_neg(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=-5)

    def test_update_kwargs_invalidheight_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(height="invalid")

    def test_updatekwargs_height_0(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(height=0)

    def test_update_kwargs_height_neg(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(height=-5)

    def test_update_kwargs_inavlid_xtype(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(x="invalid")

    def test_update_kwargs_x_neg(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(x=-5)

    def test_update_kwargs_invalid_ytype(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(y="invalid")

    def test_update_kwargs_y_neg(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(y=-5)

    def test_update_args_kwargs(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rec))

    def test_update_kwargs_wrong_key(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rec))

    def test_update_kwargs_some_wrongkeys(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(rec))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for to_dictionary of the Rectangle class"""

    def test_to_dictionary_out(self):
        rec = Rectangle(10, 2, 1, 9, 5)
        cor = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(cor, rec.to_dictionary())

    def test_to_dictionary_no_obj_changes(self):
        rec1 = Rectangle(10, 2, 1, 9, 5)
        rec2 = Rectangle(5, 9, 1, 2, 10)
        rec2.update(**rec1.to_dictionary())
        self.assertNotEqual(rec1, rec2)

    def test_to_dictionary_argument(self):
        rec = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rec.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
