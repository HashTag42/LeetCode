# LeetCode challenge: 118. Pascal's Triangle
# <https://leetcode.com/problems/pascals-triangle/description/>

import unittest
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tree = []
        if numRows == 0:
            return tree
        if numRows == 1:
            tree.append([1])
            return tree
        if numRows == 2:
            tree.append([1])
            tree.append([1, 1])
            return tree
        if numRows >= 3:
            tree.append([1])
            tree.append([1, 1])
            for i in range(2, numRows):
                row = [1]
                for j in range(1, i):
                    row.append(tree[i - 1][j - 1] + tree[i - 1][j])
                row.append(1)
                tree.append(row)
            return tree


class Generate_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test01(self):
        self.assertEqual(self.solution.generate(0), [])

    def test02(self):
        self.assertEqual(self.solution.generate(1), [[1]])

    def test03(self):
        self.assertEqual(self.solution.generate(2), [[1], [1, 1]])

    def test04(self):
        self.assertEqual(self.solution.generate(3), [[1], [1, 1], [1, 2, 1]])

    def test05(self):
        self.assertEqual(self.solution.generate(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])


if __name__ == "__main__":
    unittest.main()
