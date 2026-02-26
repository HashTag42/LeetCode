# LeetCode problem 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in '([{':
                stack.append(c)
            elif not stack or stack[-1] != pairs[c]:
                return False
            else:
                stack.pop()
        return bool(s) and len(stack) == 0
