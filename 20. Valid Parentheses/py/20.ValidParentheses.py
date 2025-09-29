# LeetCode challenge: 20. Valid Parentheses: <https://leetcode.com/problems/valid-parentheses/description/>

import unittest


################################################################################
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
################################################################################


################################################################################
class isValid_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test01(self):
        self.assertEqual(self.solution.isValid("()"), True)

    def test02(self):
        self.assertEqual(self.solution.isValid("()[]{}"), True)

    def test03(self):
        self.assertEqual(self.solution.isValid("(]"), False)

    def test04(self):
        self.assertEqual(self.solution.isValid("([])"), True)

    def test05(self):
        self.assertEqual(self.solution.isValid("([])([])"), True)

    def test06(self):
        self.assertEqual(self.solution.isValid(""), False)

    def test07(self):
        self.assertEqual(self.solution.isValid("]"), False)

    def test08(self):
        self.assertEqual(self.solution.isValid(")(){}"), False)

    def test09(self):
        self.assertEqual(self.solution.isValid("(])"), False)

    def test10(self):
        self.assertEqual(self.solution.isValid("([{}])"), True)
################################################################################


################################################################################
if __name__ == "__main__":
    unittest.main()
################################################################################
