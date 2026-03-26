'''
    LeetCode problem 167. Two Sum II - Input Array Is Sorted
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''


class Solution:
    def twoSum2(self, numbers: list[int], target: int) -> list[int] | None:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
