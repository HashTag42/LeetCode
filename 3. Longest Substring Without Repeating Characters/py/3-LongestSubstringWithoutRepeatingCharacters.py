# LeetCode challenge: 3. Longest Substring Without Repeating Characters
# <https://leetcode.com/problems/longest-substring-without-repeating-characters/description/>

import unittest


# Brute force approach
# Time Complexity: O(N^3)
# Space complexity: O(min(n,m)). We need O(k) space for checking a substring has no duplicate characters, where k is the
# size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the
# charset/alphabet m.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)

        longest_substring_length = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    longest_substring_length = max(longest_substring_length, j - i + 1)

        return longest_substring_length


class Solution_lengthOfLongestSubstring_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLongestSubstring_1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_lengthOfLongestSubstring_2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_lengthOfLongestSubstring_3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()
