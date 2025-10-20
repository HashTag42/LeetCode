# LeetCode problem 1791: Find Center of Star Graph
# https://leetcode.com/problems/find-center-of-star-graph/

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges == [] or edges is None:
            return None
        c1, c2 = edges[0][0], edges[0][1]
        c1center = True
        for node in edges:
            c1center = True if node[0] == c1 or node[1] == c1 else False
        if c1center:
            return c1
        else:
            return c2
