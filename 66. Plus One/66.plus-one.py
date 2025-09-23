# LeetCode problem: 66. Plus One
# <https://leetcode.com/problems/plus-one/>

from typing import List
import unittest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        src_number = 0
        exp_factor = 0
        for d in reversed(digits):
            src_number += d * 10 ** exp_factor
            exp_factor += 1
        dst_number = src_number + 1
        dst_list = []
        for char in str(dst_number):
            dst_list.append(int(char))
        return dst_list


class Solution_plusOne_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Case_1(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])

    def test_Case_2(self):
        self.assertEqual(self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_Case_3(self):
        self.assertEqual(self.solution.plusOne([9]), [1, 0])


if __name__ == "__main__":
    unittest.main()
