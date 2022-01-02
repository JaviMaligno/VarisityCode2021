from solution import Cinema
import unittest


class CinemaTests(unittest.TestCase):

    def test1(self):
        solution = Cinema()
        self.assertEqual(solution.find_seats(3, 3, [1, 2, 3]), 12)

    def test2(self):
        solution = Cinema()
        self.assertEqual(solution.find_seats(3, 3, [1]), 1)

    def test3(self):
        solution = Cinema()
        self.assertEqual(solution.find_seats(5, 5, [4, 5, 2, 5, 3, 1]), 62)

    def test4(self):
        solution = Cinema()
        self.assertEqual(solution.find_seats(7, 5, [4, 5, 2, 5, 3, 1]), 61)

    def test5(self):
        solution = Cinema()
        self.assertEqual(solution.find_seats(3, 3, [3, 2, 2, 2]), -1)


if __name__ == '__main__':
    unittest.main()