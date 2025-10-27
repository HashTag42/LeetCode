# LeetCode challenge: 50. Pow(x, n)
# <https://leetcode.com/problems/powx-n/description/>

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Recursive implementation:
        Time Complexity: O(n)
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        return x * self.myPow(x, n - 1)
