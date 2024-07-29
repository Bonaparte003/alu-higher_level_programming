#!/usr/bin/python3
""""max integer"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """max integer test"""

    def test_simple_case(self):
        """test simple cases"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_case(self):
        """test negative cases"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty_case(self):
        """test empty cases"""
        self.assertEqual(max_integer([]), None)

    def test_max_middle_case(self):
        """test max middle"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_one_element_case(self):
        """tests one element"""
        self.assertEqual(max_integer([5]), 5)