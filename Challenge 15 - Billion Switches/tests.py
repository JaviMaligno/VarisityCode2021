from solution import Solution
import unittest


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        self.assertEqual(solution.billion_switches([0]), 0)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.billion_switches([100]), 100)

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.billion_switches([100, 100]), 0)

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.billion_switches([100, 50, 25]), 75)


if __name__ == '__main__':
    unittest.main()