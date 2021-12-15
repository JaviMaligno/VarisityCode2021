from solution import Warehouse
import unittest

class WarehouseTests(unittest.TestCase):

    
    def test1(self):
        solution = Warehouse()
        self.assertEqual(solution.store_items("X", [ "3A:X10", "3B:X10X-5", "4C:X-5X15" ], "X10"), "3A4C")

    def test2(self):
        solution = Warehouse()
        self.assertEqual(solution.store_items("XY", [ "3A:X10", "X10:X10Y-5", "4C:X20Y-10Y5" ], "Y-5X20"), "3A4C")

    def test3(self):
        solution = Warehouse()
        self.assertEqual(solution.store_items("X", [ "3A2B:X10", "3A:X10X-5", "4C:X-5X15" ], "X10"), "2B4C6A")

if __name__ == '__main__':
    unittest.main()