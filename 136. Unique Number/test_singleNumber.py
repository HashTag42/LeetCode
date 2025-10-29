from singleNumber import Solution
import pytest


cases = [
    # nums, expected
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
]


@pytest.mark.parametrize("nums, expected", cases)
def test_Solution_singleNumber(nums, expected):
    assert Solution().singleNumber(nums) == expected
