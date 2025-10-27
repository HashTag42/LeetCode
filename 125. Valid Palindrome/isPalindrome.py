'''
LeetCode problem 125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
'''


class Solution:
    def isPalindrome1(self, s: str) -> bool:
        """
        Returns true if a string is a palindrome. False otherwise.
        Only considers alphanumeric characters in the string. Character case is ignored.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    def isPalindrome2(self, s: str) -> bool:
        """
        Returns true if a string is a palindrome. False otherwise.
        Only considers alphanumeric characters in the string. Character case is ignored.
        Two-pointer implementation.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        for i in range(len(cleaned) // 2):
            if cleaned[i] != cleaned[len(cleaned) - i - 1]:
                return False
        return True

    def isPalindrome3(self, s: str) -> bool:
        """
        Returns true if a string is a palindrome. False otherwise.
        Only considers alphanumeric characters in the string. Character case is ignored.
        Two-pointer implementation.
        Does not make a copy of the source string.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
