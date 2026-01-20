'''
LeetCode problem 392. Is Subsequence
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.
'''


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        '''
        Returns True if s is a subsequence of t, or False otherwise.

        Time complexity: O(len(s) + len(t))
        Space complexity: O(len(s))
        '''
        accumulated = ''
        t_idx = 0
        for s_idx in range(len(s)):
            next_char = s[s_idx]
            for j in range(t_idx, len(t)):
                if t[j] == next_char:
                    accumulated += next_char
                    t_idx = j + 1
                    break
        if accumulated == s:
            return True
        return False
