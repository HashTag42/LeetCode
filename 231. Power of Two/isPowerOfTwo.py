'''
LeetCode problem 231. Power of Two
https://leetcode.com/problems/power-of-two/
'''
import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in range(int(math.sqrt(n)) + 2):
            if pow(2, i) == float(n):
                return True

        return False
