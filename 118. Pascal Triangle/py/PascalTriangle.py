# LeetCode challenge: 118. Pascal's Triangle
# <https://leetcode.com/problems/pascals-triangle/description/>

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

        tree.append([1])
        tree.append([1, 1])
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(tree[i - 1][j - 1] + tree[i - 1][j])
            row.append(1)
            tree.append(row)
        return tree
