# LeetCode problem 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dirty = False
        for i in s:
            if i in ['(', '[', '{'] or len(stack) == 0:
                stack.append(i)
                dirty = True
            elif len(stack) > 0:
                sub = stack[-1] + i
                if sub in ['()', '[]', '{}']:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0 and dirty:
            return True
        else:
            return False
