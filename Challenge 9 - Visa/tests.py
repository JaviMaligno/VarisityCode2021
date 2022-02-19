from solution import Clearing
import unittest


class ClearingTests(unittest.TestCase):

    def test1(self):
        solution = Clearing()
        self.assertEqual(solution.calculate_settlement([1021542593], [0], [0], [1], [5]), [0])

    def test2(self):
        solution = Clearing()
        self.assertEqual(solution.calculate_settlement([1], [0], [0], [0], [0]), [0])

    def test3(self):
        solution = Clearing()
        self.assertEqual(solution.calculate_settlement(
            [42424242, 42424243, 42424244, 42424245, 42424246, 42424247, 42424248, 42424249, 42424250, 42424251,
             42424252, 42424253, 42424254, 42424255, 42424256, 42424257, 42424258, 42424259, 42424260, 42424261,
             42424262, 42424263, 42424264, 42424265, 42424266, 42424267, 42424268, 42424269, 42424270, 42424271,
             42424272, 42424273, 42424274, 42424275, 42424276, 42424277, 42424278, 42424279, 42424280, 42424281,
             42424282, 42424283],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0]),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                          28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41])

    def test4(self):
        solution = Clearing()
        self.assertEqual(
            solution.calculate_settlement([84975729, 14134739, 26867459], [5808, 343, 826], [7, 2, 4], [1, 6, 7],
                                          [4, 6, 2]),
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 826, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5808,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 343, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test5(self):
        solution = Clearing()
        self.assertEqual(
            solution.calculate_settlement([53879381, 72823039, 51127541], [10, 20, 30], [1, 1, 5], [1, 1, 1],
                                          [1, 1, 1]),
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test6(self):
        solution = Clearing()
        self.assertEqual(solution.calculate_settlement(
            [17325415, 34216871, 27347119, 71773775, 76309649, 57802873, 69776087, 31103053],
            [750, 233, 46123, 5996, 593, 0, 176, 0], [5, 2, 0, 2, 0, 1, 5, 2], [0, 7, 1, 0, 1, 7, 5, 5],
            [5, 0, 0, 6, 2, 3, 4, 3]), [2, 4])

    def test7(self):
        solution = Clearing()
        self.assertEqual(solution.calculate_settlement([], [], [], [], []),
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0])

if __name__ == '__main__':
    unittest.main()