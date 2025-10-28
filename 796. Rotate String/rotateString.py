'''
LeetCode problem 796. Rotate String
https://leetcode.com/problems/rotate-string/
'''


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def shiftLeft(s: str) -> str:
            return s[1:] + s[0]

        length = len(s)
        for _ in range(length):
            shifted = shiftLeft(s)
            if shifted == goal:
                return True
            s = shifted

        return False
