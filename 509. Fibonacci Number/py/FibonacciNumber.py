# LeetCode problem 509. Fibonacci Number
# <https://leetcode.com/problems/fibonacci-number/>

class Solution:
    def fib(self, n: int) -> int:
        if n < 0:
            raise ValueError("Number must be a positive integer")
        elif n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                c = a + b
                a = b
                b = c
            return c
