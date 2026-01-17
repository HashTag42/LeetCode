'''
LeetCode problem 219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/

Given an integer array `nums` and an integer `k`, return `true`
if there are two distinct indices `i` and `j` in the array
such that `nums[i] == nums[j]` and `abs(i - j) <= k`.
'''


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    '''
    Runtime complexity: O(n)
    Space complexity: O(n)
    '''
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False
