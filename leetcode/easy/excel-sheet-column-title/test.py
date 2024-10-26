import unittest
from main import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_letter_columns(self):
        self.assertEqual(self.solution.convertToTitle(1), "A")
        self.assertEqual(self.solution.convertToTitle(26), "Z")

    def test_double_letter_columns(self):
        self.assertEqual(self.solution.convertToTitle(27), "AA")
        self.assertEqual(self.solution.convertToTitle(52), "AZ")
        self.assertEqual(self.solution.convertToTitle(53), "BA")

    def test_triple_letter_columns(self):
        self.assertEqual(self.solution.convertToTitle(703), "AAA")
        self.assertEqual(self.solution.convertToTitle(728), "AAZ")
        self.assertEqual(self.solution.convertToTitle(729), "ABA")

    def test_large_numbers(self):
        self.assertEqual(self.solution.convertToTitle(18278), "ZZZ")
        self.assertEqual(self.solution.convertToTitle(18279), "AAAA")


if __name__ == "__main__":
    unittest.main()
