from missingNumber import Solution
import pytest


@pytest.mark.parametrize("nums,expected", [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
])
def test__Solution_missingNumber(nums, expected):
    sol = Solution()
    assert expected == sol.missingNumber(nums)
