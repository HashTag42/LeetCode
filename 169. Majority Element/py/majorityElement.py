'''
LeetCode problem 169. Majority Element
https://leetcode.com/problems/majority-element/description/
'''


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Returns the element that appears more in an array (list)
        Implementation using Boyer-Moore Voting Algorithm
        Time complexity = O(n)
        Space complexity = O(1)
        """
        candidate, count = nums[0], 0
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate
