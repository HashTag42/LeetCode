from find_difference import find_difference
import pytest


test_cases = [
    # (nums1, nums2, expected)
    ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
    ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
]


@pytest.mark.parametrize('nums1, nums2, expected', test_cases)
def test_find_difference(nums1, nums2, expected):
    assert find_difference(nums1, nums2) == expected
