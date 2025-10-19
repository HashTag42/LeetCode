# LeetCode problem 70. Climbing Stairs
# <https://leetcode.com/problems/climbing-stairs/description/>

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fibonacci(n)

    def fibonacci(self, n: int) -> int:
        if n <= 0:
            raise ValueError()
        elif n == 1:
            return 1
        else:
            a = 1
            b = 2
        for _ in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b
