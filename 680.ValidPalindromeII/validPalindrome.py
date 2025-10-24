# LeetCode problem #680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/description/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Checks if a string is a palindrome when removing up to 1 character.
        Two-pointer solution.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        def is_palindrome_range(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Try skipping either the left or right character
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1
        return True
