'''
LeetCode problem 202. Happy Number
https://leetcode.com/problems/happy-number/description/
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        while True:
            n = sum(int(c) ** 2 for c in str(n))
            if n == 1:
                return True
            if n in results:
                return False
            results.add(n)
