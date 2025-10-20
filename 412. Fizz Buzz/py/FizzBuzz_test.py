import unittest
from FizzBuzz import Solution


class Solution_fizzBuzz_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Case1(self):
        self.assertEqual(self.solution.fizzBuzz(3), ["1", "2", "Fizz"])

    def test_Case2(self):
        self.assertEqual(self.solution.fizzBuzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_Case3(self):
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                    "11", "Fizz", "13", "14", "FizzBuzz"]
        self.assertEqual(self.solution.fizzBuzz(15), expected)
