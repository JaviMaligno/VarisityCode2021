from solution import FraudAlert
import unittest


class FraudAlertTests(unittest.TestCase):

    def test1(self):
        solution = FraudAlert()
        self.assertEqual(solution.detect_outliers([1, 0, 0.5, 1, 0, 0, -1.8, 0.2, -1, -1.32]), [])

    def test2(self):
        solution = FraudAlert()
        self.assertEqual(solution.detect_outliers(
            [10, 10, -10, -10, 11, 10, -13, -12, 15, 18, 9, 11, -12, -8, -13, -12, -15, -10, 0, -13]), [15, 18, 0, -13])


if __name__ == '__main__':
    unittest.main()