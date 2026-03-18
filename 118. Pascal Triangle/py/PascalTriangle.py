# LeetCode challenge: 118. Pascal's Triangle
# <https://leetcode.com/problems/pascals-triangle/description/>

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # LeetCode constraint: 1 <= numRows <= 32
        tree = [[1]]
        for i in range(1, numRows):
            row = [1] + [tree[i-1][j-1] + tree[i-1][j] for j in range(1, i)] + [1]
            tree.append(row)
        return tree
