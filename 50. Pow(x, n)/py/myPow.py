# LeetCode problem: 50. Pow(x, n)
# <https://leetcode.com/problems/powx-n/description/>

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Algorithm: Binary Exponentiation
        Time Complexity: O(log n)
        """
        if n == 0:
            return 1
        if n < 0:
            x, n = 1 / x, -n
        result = 1
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result
