# LeetCode challenge: 3. Longest Substring Without Repeating Characters
# <https://leetcode.com/problems/longest-substring-without-repeating-characters/description/>

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brute force approach
        Time Complexity: O(N^3)
        Space complexity: O(min(n,m)). We need O(k) space for checking a substring has no duplicate characters, where k
        is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the
        charset/alphabet m.
        """
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
