from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:2;2:4;3.5:7;4:8"), "1:2;2:4;3.5:7;4:8")

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;2:5;3:3;4:6"), "KEEP_PREVIOUS")

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;1:2;3:3;4:4"), "KEEP_PREVIOUS")

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;2:2;3.5:3.5;4:5"), "1:1;2:2;3.5:3.5;4:4")

if __name__ == '__main__':
    unittest.main()