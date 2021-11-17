# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 23:47:40 2021

@author: javia
"""

from solution import ShoppingBag
import unittest

class ShoppingBagTests(unittest.TestCase):

    
    def test1(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123" ], [ "ABC1P10" ]), 110.7)

    def test2(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC123" ], [ "ABC1C10" ]), 113)

    def test3(self):
        solution = ShoppingBag()
        self.assertEqual(solution.calculate_bag_total([ "ABC010", "DEF020", "ABC010" ], [ "ABC2P50", "DEF1C05" ]), 25)

if __name__ == '__main__':
    unittest.main()