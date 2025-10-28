from intersection import Solution
import pytest


cases = [
    ([], [], []),
    ([1], [], []),
    ([], [1], []),
    ([1], [1], [1]),
    ([1], [2], []),
    ([1, 2, 2, 1], [2, 2], [2]),
    ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
]


@pytest.mark.parametrize("nums1, nums2, expected", cases)
def test_Solution_intersection(nums1, nums2, expected):
    solution = Solution()
    assert solution.intersection(nums1, nums2) == expected
