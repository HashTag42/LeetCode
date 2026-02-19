# LeetCode challenge: 3. Longest Substring Without Repeating Characters
# <https://leetcode.com/problems/longest-substring-without-repeating-characters/description/>

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window approach
        Time Complexity: O(N)
        Space Complexity: O(min(N, M)) where M is the charset size
        """
        char_index = {}
        left = 0
        max_len = 0

        for right, c in enumerate(s):
            if c in char_index and char_index[c] >= left:
                left = char_index[c] + 1
            char_index[c] = right
            max_len = max(max_len, right - left + 1)

        return max_len

