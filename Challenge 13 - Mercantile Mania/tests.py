from solution import MatchingEngine
import unittest


class MatchingEngineTests(unittest.TestCase):

    def test1(self):
        solution = MatchingEngine()
        self.assertEqual(solution.handle_orders(["10,B,10.5000,50,C001", "12,A,10.5000,25,C002"]),
                         ["12,10.5000,25,C001,C002"])

    def test2(self):
        solution = MatchingEngine()
        self.assertEqual(solution.handle_orders(
            ["10,A,50.8000,20,C001", "12,A,51.4000,50,C010", "18,B,51.5000,60,C002", "19,A,51.6000,40,C001",
             "25,B,50.9000,10,C132", "28,B,51.6000,70,C007", "31,A,51.0000,45,C011"]),
                         ["18,50.8000,20,C001,C002", "18,51.4000,40,C010,C002", "28,51.4000,10,C010,C007",
                          "28,51.6000,40,C001,C007", "31,51.6000,20,C007,C011"])


if __name__ == '__main__':
    unittest.main()