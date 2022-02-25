from solution import Calendar
import unittest


class CalendarTests(unittest.TestCase):

    def test1(self):
        solution = Calendar()
        self.assertEqual(solution.get_repeating_event("2021/10/14", "every 3 days"),
                         ["2021/10/14", "2021/10/17", "2021/10/20", "2021/10/23"])

    def test2(self):
        solution = Calendar()
        self.assertEqual(solution.get_repeating_event("2021/04/04", "every 1 week"),
                         ["2021/04/04", "2021/04/11", "2021/04/18", "2021/04/25"])

    def test3(self):
        solution = Calendar()
        self.assertEqual(solution.get_repeating_event("2021/12/21", "every 8 months"),
                         ["2021/12/21", "2022/08/21", "2023/04/21", "2023/12/21"])

    def test4(self):
        solution = Calendar()
        self.assertEqual(solution.get_repeating_event("2021/07/09", "every 10 years"),
                         ["2021/07/09", "2031/07/09", "2041/07/09", "2051/07/09"])

    def test5(self):
        solution = Calendar()
        self.assertEqual(solution.get_repeating_event("2021/01/01", "every foo bar"), [])

if __name__ == '__main__':
    unittest.main()