from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(8), 4)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(36), 10)

if __name__ == '__main__':
    unittest.main()