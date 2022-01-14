from solution import ReportingData
import unittest


class ReportingDataTests(unittest.TestCase):

    def test1(self):
        solution = ReportingData()
        self.assertEqual(solution.cleaner(["60", "36", "24", "22"]), [60, 36, 24, 22])

    def test2(self):
        solution = ReportingData()
        self.assertEqual(solution.cleaner(["55", "55", "n/a", "0"]), [55, 55, 0, 0])

    def test3(self):
        solution = ReportingData()
        self.assertEqual(solution.cleaner(["50", "50", "0"]), [50, 50, 0, 0])

    def test4(self):
        solution = ReportingData()
        self.assertEqual(solution.cleaner(["60", "36", "4", "20"]), [60, 36, 24, 20])

    def test5(self):
        solution = ReportingData()
        self.assertEqual(solution.cleaner(["60", "60%", "24", "22"]), [60, 36, 24, 22])
    def test6(self):
        solution = ReportingData()
        self.assertEqual(solution.cleaner([ "80", "-", "50", "25" ]), [ 80, 30, 50, 25 ])

    def test7(self):
        solution = ReportingData()
        self.assertEqual(solution.cleaner([ "50", "70", "0", "0" ]), [ 50, 0, 0, 0 ])

if __name__ == '__main__':
    unittest.main()