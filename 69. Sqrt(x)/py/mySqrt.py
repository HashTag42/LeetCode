# Leet Code challenge: 69. Sqrt(x)
# <https://leetcode.com/problems/sqrtx/>

class Solution:
    def mySqrt(self, x: int) -> int:
        previous, current = 0, 0
        while True:
            previous = current
            current += 1
            sum = current * current
            if sum > x:
                return previous
