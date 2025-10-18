from missingNumber import Solution
import pytest


cases = [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
]


@pytest.mark.parametrize("nums,expected", cases)
def test__Solution_missingNumber1(nums, expected):
    sol = Solution()
    assert expected == sol.missingNumber1(nums)


@pytest.mark.parametrize("nums,expected", cases)
def test__Solution_missingNumber2(nums, expected):
    sol = Solution()
    assert expected == sol.missingNumber2(nums)
