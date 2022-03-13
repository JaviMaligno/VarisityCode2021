from solution import TransmissionIntegrity
import unittest


class TransmissionIntegrityTests(unittest.TestCase):

    def test1(self):
        solution = TransmissionIntegrity()
        self.assertEqual(solution.fix_message("2b8e"), "2b8e")

    def test2(self):
        solution = TransmissionIntegrity()
        self.assertEqual(solution.fix_message("2bae"), "2b8e")


if __name__ == '__main__':
    unittest.main()