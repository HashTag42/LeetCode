# LeetCode problem: 66. Plus One
# <https://leetcode.com/problems/plus-one/>

from typing import List


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
