# LeetCode problem 1791: Find Center of Star Graph
# https://leetcode.com/problems/find-center-of-star-graph/

import unittest
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c1, c2 = edges[0][0], edges[0][1]
        c1center = True
        c2center = True
        for node in edges:
            c1center = True if node[0] == c1 or node[1] == c1 else False
            c2center = True if node[0] == c2 or node[1] == c2 else False
        if c1center:
            return c1
        elif c2center:
            return c2


class Solution_findCenter_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findCenter_Case_1(self):
        self.assertEqual(self.solution.findCenter([[1, 2], [2, 3], [4, 2]]), 2)

    def test_findCenter_Case_2(self):
        self.assertEqual(self.solution.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]), 1)


if __name__ == "__main__":
    unittest.main()
