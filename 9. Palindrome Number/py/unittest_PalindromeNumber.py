import unittest
from PalindromeNumber import Solution


class Test_unittest_PalindromeNumber(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.isPalindrome(121), True)

    def test_2(self):
        self.assertEqual(self.solution.isPalindrome(-121), False)

    def test_3(self):
        self.assertEqual(self.solution.isPalindrome(10), False)


if __name__ == '__main__':
    unittest.main()
