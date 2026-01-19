from next_greater_element import next_greater_element
import pytest

test_cases = [
    # nums1, nums2, expected
    ([1], [1], [-1]),
    ([1], [1, 2], [2]),
    ([1], [1, 2, 3], [2]),
    ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
    ([2, 4], [1, 2, 3, 4], [3, -1]),
]


@pytest.mark.parametrize('nums1, nums2, expected', test_cases)
def test_next_greater_element(nums1, nums2, expected):
    assert next_greater_element(nums1, nums2) == expected
