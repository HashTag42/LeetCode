# LeetCode challenge: 733. Flood Fill <https://leetcode.com/problems/flood-fill/description/>

from typing import List
from collections import deque
import unittest

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
    # Complexity Analysis:
    # Time Complexity: O(N), where N is the number of pixels in the image. We might process every pixel.
    # Space Complexity: O(N), the size of the implicit call stack when calling dfs.
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r-1, c)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < C:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image        

class floodFill_Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    def test01(self):
        image    = [[1,1,1],[1,1,0],[1,0,1]]
        sr, sc, color = 1, 1, 2
        expected = [[2,2,2],[2,2,0],[2,0,1]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test02(self):
        image    = [[0,0,0],[0,0,0]]
        sr, sc, color = 0, 0, 0
        expected = [[0,0,0],[0,0,0]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test03(self):
        image =    [[0]]
        sr, sc, color = 0, 0, 0
        expected = [[0]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test04(self):
        image    = [[0]]
        sr, sc, color = 0, 0, 2
        expected = [[2]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test05(self):
        image    = [[1,1],[1,0]]
        sr, sc, color = 0, 0, 2
        expected = [[2,2],[2,0]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test06(self):
        image    = [[1,1],[0,1]]
        sr, sc, color = 0, 0, 2
        expected = [[2,2],[0,2]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test07(self):
        image    = [[1,0],[1,1]]
        sr, sc, color = 0, 0, 2
        expected = [[2,0],[2,2]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test08(self):
        image    = [[0,1],[1,1]]
        sr, sc, color = 1, 1, 2
        expected = [[0,2],[2,2]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test09(self):
        image    = [[0,1],[1,1]]
        sr, sc, color = 1, 0, 2
        expected = [[0,2],[2,2]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test10(self):
        image    = [[0,1],[1,1]]
        sr, sc, color = 0, 1, 2
        expected = [[0,2],[2,2]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test11(self):
        image    = [[0,1,0],[1,1,1],[0,1,0]]
        sr, sc, color = 1, 1, 2
        expected = [[0,2,0],[2,2,2],[0,2,0]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test12(self):
        image    = [[1,1,1]]
        sr, sc, color = 0, 0, 2
        expected = [[2,2,2]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test13(self):
        image    = [[0,1,1]]
        sr, sc, color = 0, 1, 2
        expected = [[0,2,2]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def test14(self):
        image    = [[1,1,1]]
        sr, sc, color = 0, 2, 2
        expected = [[2,2,2]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), expected)
    def tearDown(self):
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()