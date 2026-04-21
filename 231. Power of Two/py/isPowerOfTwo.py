'''
LeetCode problem 231. Power of Two
https://leetcode.com/problems/power-of-two/
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
