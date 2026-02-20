# LeetCode problem: 9. Palindrome Number
# <https://leetcode.com/problems/palindrome-number/description/>

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Time Complexity = O(N)
        # Space Complexity = O(N)
        strX = str(x)
        lenX = len(strX)
        for i in range(lenX // 2):
            if strX[i] != strX[lenX - 1 - i]:
                return False
        return True
