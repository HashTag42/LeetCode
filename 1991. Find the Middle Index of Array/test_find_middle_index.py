from find_middle_index import find_middle_index
import pytest

test_cases = [
    # (nums, expected)
    ([2, 3, -1, 8, 4], 3),
    ([1, -1, 4], 2),
    ([2, 5], -1),
]


@pytest.mark.parametrize('nums, expected', test_cases)
def test_find_middle_index(nums, expected):
    assert find_middle_index(nums) == expected
