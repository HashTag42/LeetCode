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
    ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
    ([2, 4], [1, 2, 3, 4], [3, -1]),
]
'''


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    ans: list[int] = []
    for n1 in nums1:
        found: bool = False
        greater: int = -2
        for n2 in nums2:
            if found and n2 > n1:
                ans.append(n2)
                greater = n2
                break
            if n1 == n2:
                found = True
        if not found or greater == -2:
            ans.append(-1)
    return ans
