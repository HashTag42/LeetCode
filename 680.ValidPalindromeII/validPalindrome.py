# LeetCode problem #680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/description/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Returns true if the str s can be a palindrome by removing 0 or 1 characters from it. False otherwise.
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        for i in range(len(s)):
            copy = s[:i] + s[i + 1:]
            if copy == copy[::-1]:
                return True

        return False
