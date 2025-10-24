# LeetCode problem #680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/description/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        for i in range(len(s)):
            copy = s[:i] + s[i + 1:]
            if copy == copy[::-1]:
                return True

        return False
