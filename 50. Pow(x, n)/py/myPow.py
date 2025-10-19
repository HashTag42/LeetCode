# LeetCode challenge: 50. Pow(x, n)
# <https://leetcode.com/problems/powx-n/description/>

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time Complexity: O(N)
        if n > 0:
            expo = x
            for _ in range(1, n):
                expo *= x
        elif n == 0:
            expo = 1
        else:   # n < 0
            expo = 1 / x
            for _ in range(1, abs(n)):
                expo /= x
        return expo
