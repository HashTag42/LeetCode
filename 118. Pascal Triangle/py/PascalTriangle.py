# LeetCode problem: 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/description/


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # LeetCode constraint: 1 <= numRows <= 30
        tree = [[1]]
        for i in range(1, numRows):
            row = [1] + [tree[i-1][j-1] + tree[i-1][j] for j in range(1, i)] + [1]
            tree.append(row)
        return tree
