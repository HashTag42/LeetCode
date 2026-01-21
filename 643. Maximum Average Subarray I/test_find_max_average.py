from find_max_average import find_max_average
import pytest

test_cases = [
    # (nums, k, expected)
    ([1, 12, -5, -6, 50, 3], 4, 12.75000),
    ([5], 1, 5.00000),
    ([-1], 1, -1.00000),
    ([0, 4, 0, 3, 2], 1, 4.00000),
    ([6, 8, 6, 8, 0, 4, 1, 2, 9, 9], 2, 9.00000),
]


@pytest.mark.parametrize('nums, k, expected', test_cases)
def test_find_max_average(nums, k, expected):
    assert find_max_average(nums, k) == expected
