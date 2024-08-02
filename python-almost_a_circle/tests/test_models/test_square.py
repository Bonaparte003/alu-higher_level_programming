#!/usr/bin/python3


"""square unit testing"""


import sys
import io
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instant(unittest.TestCase):
    """Unittests for instantition of the Square"""

    def test_is_Base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_Rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_argumentss(self):
        with self.assertRaises(TypeError):
            Square()

    def test_1_arg(self):
        sq1 = Square(10)
        sq2 = Square(11)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_2_args(self):
        sq1 = Square(10, 2)
        sq2 = Square(2, 10)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_3_args(self):
        sq1 = Square(10, 2, 2)
        sq2 = Square(2, 2, 10)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_4_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more__than4_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_is_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getting(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setting(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 8
        self.assertEqual(8, sq.size)

    def test_width_geting(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 8
        self.assertEqual(8, sq.width)

    def test_height_getting(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 8
        self.assertEqual(8, sq.height)

    def test_x_geting(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getting(self):
        self.assertEqual(0, Square(10).y)


class TestSquare_init(unittest.TestCase):
    """Unittests for size init of square"""

    def test_No_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_string_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_floating_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complx_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dictiosize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    '''def test_boolean_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)'''

    def test_l_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_setsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuples_with_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozensetsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_with_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytessize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Bytes')

    def test_bytearraysize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_memoryviewsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_infsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nansize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_neg_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_0_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """testing x attribute."""

    def test_No_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_floating_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_complx_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dictx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    '''def test_boolean_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)'''

    def test_listx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_setx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuples_wiht_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_frozensetx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_rangex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def test_bytesx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Bytec')

    def test_bytearrayx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefghi'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfghi'))

    def test_infx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def test_nanx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquare_y(unittest.TestCase):
    """testing init of Square y attribute."""

    def test_No_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_floating_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_complx_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_dicty(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def test_l_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_sety(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_tuples_with_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def test_frozensety(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({1, 2, 3, 1}))

    def test_rangey(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    def test_bytesy(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'Python')

    def test_bytearrayy(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'abcdefg'))

    def test_memoryviewy(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b'abcedfg'))

    def test_infy(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    def test_nany(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquare_order_of_init(unittest.TestCase):
    """testing order of Square attribute init"""

    def test_size_beforex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_beforey(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_beforey(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquare_for_area(unittest.TestCase):
    """Unittests area method of the Square class"""

    def test_areasmall(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_arealarge(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changedattributes(self):
        sq = Square(2, 0, 0, 1)
        sq.size = 7
        self.assertEqual(49, sq.area())

    def test_area_1_arg(self):
        sq = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            sq.area(1)


class TestSquare_stdout_put(unittest.TestCase):
    """Unittests display methods of Square class"""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdou"""
        capt = io.StringIO()
        sys.stdout = capt
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capt

    def test_str_method_printsize(self):
        sq = Square(4)
        capt = TestSquare_stdout_put.capture_stdout(sq, "print")
        cor = "[Square] ({}) 0/0 - 4\n".format(sq.id)
        self.assertEqual(cor, capt.getvalue())

    def test_str_method_sizex(self):
        sq = Square(5, 5)
        cor = "[Square] ({}) 5/0 - 5".format(sq.id)
        self.assertEqual(cor, sq.__str__())

    def test_str_method_size_xy(self):
        sq = Square(7, 4, 22)
        cor = "[Square] ({}) 4/22 - 7".format(sq.id)
        self.assertEqual(cor, str(sq))

    def test_str_method_size_xy_id(self):
        sq = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(sq))

    def test_str_method_changed_att(self):
        sq = Square(7, 0, 0, [4])
        sq.size = 15
        sq.x = 8
        sq.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(sq))

    def test_str_method_1_arg(self):
        sq = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            sq.__str__(1)

    def test_displaysize(self):
        sq = Square(2, 0, 0, 9)
        capt = TestSquare_stdout_put.capture_stdout(sq, "display")
        self.assertEqual("##\n##\n", capt.getvalue())

    def test_display_sizex(self):
        sq = Square(3, 1, 0, 18)
        capt = TestSquare_stdout_put.capture_stdout(sq, "display")
        self.assertEqual(" ###\n ###\n ###\n", capt.getvalue())

    def test_display_sizey(self):
        sq = Square(4, 0, 1, 9)
        capt = TestSquare_stdout_put.capture_stdout(sq, "display")
        disp = "\n####\n####\n####\n####\n"
        self.assertEqual(disp, capt.getvalue())

    def test_display_size_xy(self):
        sq = Square(2, 3, 2, 1)
        capt = TestSquare_stdout_put.capture_stdout(sq, "display")
        disp = "\n\n   ##\n   ##\n"
        self.assertEqual(disp, capt.getvalue())

    def test_display_1_arg(self):
        sq = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            sq.display(1)


class TestSquare_update_arg(unittest.TestCase):
    """Unittests args method of the Square"""

    def test_update_args_0(self):
        sq = Square(10, 10, 10, 10)
        sq.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(sq))

    def test_update_args_1(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(sq))

    def test_update_args_2(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(sq))

    def test_update_args_3(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(sq))

    def test_update_args_4(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sq))

    def test_update_args_more(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sq))

    def test_update_args_width_setting(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        self.assertEqual(2, sq.width)

    def test_update_args_height_setting(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        self.assertEqual(2, sq.height)

    def test_update_args_No_id(self):
        sq = Square(10, 10, 10, 10)
        sq.update(None)
        cor = "[Square] ({}) 10/10 - 10".format(sq.id)
        self.assertEqual(cor, str(sq))

    def test_update_args_No_id_and_more(self):
        sq = Square(10, 10, 10, 10)
        sq.update(None, 4, 5)
        cor = "[Square] ({}) 5/10 - 4".format(sq.id)
        self.assertEqual(cor, str(sq))

    def test_update_arguments_twice(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4)
        sq.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(sq))

    def test_update_arguments_invalid_size_type(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(89, "invalid")

    def test_update_args_size_0(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(89, 0)

    def test_update_args_size_neg(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(89, -4)

    def test_update_args_invalidx(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(89, 1, "invalid")

    def test_update_args_x_neg(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(98, 1, -4)

    def test_update_args_invalidy(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(89, 1, 2, "invalid")

    def test_update_args_y_neg(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(98, 1, 2, -4)

    def test_update_args_size_beforex(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(89, "invalid", "invalid")

    def test_update_args_size_beforey(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(89, "invalid", 2, "invalid")

    def test_update_args_x_beforeqy(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(89, 1, "invalid", "invalid")


class TestSquare_updatekwargs(unittest.TestCase):
    """Unittests kwargs method of Square"""

    def test_update_kwargs_1(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(sq))

    def test_update_kwargs_2(self):
        sq = Square(10, 10, 10, 10)
        sq.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(sq))

    def test_update_kwargs_3(self):
        sq = Square(10, 10, 10, 10)
        sq.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(sq))

    def test_update_kwargs_4(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(sq))

    def test_update_kwargs_width_setting(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, size=8)
        self.assertEqual(8, sq.width)

    def test_update_kwargs_heightsetter(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, size=9)
        self.assertEqual(9, sq.height)

    def test_update_kwargs_No_id(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=None)
        cor = "[Square] ({}) 10/10 - 10".format(sq.id)
        self.assertEqual(cor, str(sq))

    def test_update_kwargs_None_id_and_more(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=None, size=7, x=18)
        cor = "[Square] ({}) 18/10 - 7".format(sq.id)
        self.assertEqual(cor, str(sq))

    def test_update_kwargstwice(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, x=1)
        sq.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(sq))

    def test_update_kwargs_invalidsize(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(size="invalid")

    def test_update_kwargs_size_0(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=0)

    def test_update_kwargs_size_neg(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=-3)

    def test_update_kwargs_invalidx(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(x="invalid")

    def test_update_kwargs_x_neg(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(x=-5)

    def test_update_kwargs_invalidy(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(y="invalid")

    def test_update_kwargs_y_neg(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(y=-5)

    def test_update_args_kwargs(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(sq))

    def test_update_kwargs_keys(self):
        sq = Square(10, 10, 10, 10)
        sq.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(sq))

    def test_update_kwargs_some_wrong_k(self):
        sq = Square(10, 10, 10, 10)
        sq.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(sq))


class TestSquare_to_dic(unittest.TestCase):
    """Unittests for testing to_dictionary"""

    def test_to_dictionary_out(self):
        sq = Square(10, 2, 1, 1)
        cor = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(cor, sq.to_dictionary())

    def test_to_dictionary_no_obj_changes(self):
        sq1 = Square(10, 2, 1, 2)
        sq2 = Square(1, 2, 10)
        sq2.update(**sq1.to_dictionary())
        self.assertNotEqual(sq1, sq2)

    def test_to_dictionary_argument(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            sq.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
