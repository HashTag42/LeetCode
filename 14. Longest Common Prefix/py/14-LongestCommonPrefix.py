# LeetCode challenge: 14. Longest Common Prefix
# <https://leetcode.com/problems/longest-common-prefix/description/>

import unittest
from typing import List


class Solution:

    ''' Find the longest common prefix string among an array of strings.
        If there is no common prefix, return an empty string"". '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        common_prefix = ""
        i = 0
        while (True):
            if i >= len(strs[0]):
                break
            char = strs[0][i]
            for s in strs:
                if i >= len(s) or char != s[i]:
                    return common_prefix
            common_prefix += char
            i += 1
        return common_prefix


class longestCommonPrefix_tests(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_common_prefix(self):
        self.assertEqual(self.s.longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test_no_common_prefix(self):
        self.assertEqual(self.s.longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_single_character_string_1(self):
        self.assertEqual(self.s.longestCommonPrefix(["a", "ab"]), "a")

    def test_single_character_string_2(self):
        self.assertEqual(self.s.longestCommonPrefix(["ab", "a"]), "a")

    def test_repeated_strings(self):
        self.assertEqual(self.s.longestCommonPrefix(["dog", "dog", "dog"]), "dog")

    def test_one_string(self):
        self.assertEqual(self.s.longestCommonPrefix(["yadda"]), "yadda")

    def test_no_strings(self):
        self.assertEqual(self.s.longestCommonPrefix([]), "")

    def test_empty_string(self):
        self.assertEqual(self.s.longestCommonPrefix([""]), "")

    def test_empty_strings(self):
        self.assertEqual(self.s.longestCommonPrefix(["", ""]), "")

    def test_string_vs_empty_string(self):
        self.assertEqual(self.s.longestCommonPrefix(["hello", ""]), "")

    def test_empty_string_vs_string(self):
        self.assertEqual(self.s.longestCommonPrefix(["", "bye"]), "")


if __name__ == "__main__":
    unittest.main()
