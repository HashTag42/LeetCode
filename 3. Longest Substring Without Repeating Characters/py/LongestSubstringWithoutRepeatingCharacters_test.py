import unittest
from LongestSubstringWithoutRepeatingCharacters import Solution


class Solution_lengthOfLongestSubstring_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLongestSubstring_1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_lengthOfLongestSubstring_2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_lengthOfLongestSubstring_3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)
