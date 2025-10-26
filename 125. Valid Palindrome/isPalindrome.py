'''
LeetCode problem 125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Returns true if a string is a palindrome. False otherwise.
        Only considers alphanumeric characters. Character case is ignored.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]
