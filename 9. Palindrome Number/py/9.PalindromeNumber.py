# LeetCode problem: 9. Palindrome Number: <https://leetcode.com/problems/palindrome-number/description/>

import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
    # Time Complexity = O(N)
    # Space Complexity = O(1)
        strX = str(x)
        lenX = len(strX)
        for i in range(lenX - 1):
            if strX[i] != strX[lenX - 1 - i]:
                return False
        return True
    
class Solution_isPalindrome_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test1(self):
        self.assertEqual(self.solution.isPalindrome(121), True)
    def test2(self):
        self.assertEqual(self.solution.isPalindrome(-121), False)
    def test3(self):
        self.assertEqual(self.solution.isPalindrome(10), False)

if __name__ == "__main__":
    unittest.main()
