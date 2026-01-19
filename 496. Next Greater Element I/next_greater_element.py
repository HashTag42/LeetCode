'''
LeetCode problem 496. Next Greter Element I
https://leetcode.com/problems/next-greater-element-i/

The next greater element of some element `x` in an array is the
first greater element that is to the right of `x` in the same array.

You are given two distinct 0-indexed integer arrays `nums1` and `nums2`,
where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]`
and determine the next greater element of `nums2[j]` in `nums2`.
If there is no next greater element, then the answer for this query is `-1`.

Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element
as described above.

Constraints:

* `1 <= nums1.length <= nums2.length <= 1000`
* `0 <= nums1[i], nums2[i] <= 104`
* All integers in `nums1` and `nums2` are unique.
* All the integers of `nums1` also appear in `nums2`.

test_cases = [
    # nums1, nums2, expected
    ([1], [1], [-1]),
    ([1], [1, 2], [2]),
    ([1], [1, 2, 3], [2]),
    ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
    ([2, 4], [1, 2, 3, 4], [3, -1]),
]
'''


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    '''
    Time complexity: O(len(nums1) * len(nums2))
    Space complexity: O(len(nums1))
    '''
    ans = []
    for n1 in nums1:
        idx = nums2.index(n1)
        next_greater = -1
        for n2 in nums2[idx+1:]:
            if n2 > n1:
                next_greater = n2
                break
        ans.append(next_greater)
    return ans
