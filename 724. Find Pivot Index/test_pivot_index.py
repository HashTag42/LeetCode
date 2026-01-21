from pivot_index import pivot_index
import pytest


test_cases = [
    # (nums, expected)
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0),
]


@pytest.mark.parametrize('nums, expected', test_cases)
def test_pivot_index(nums, expected):
    assert pivot_index(nums) == expected
