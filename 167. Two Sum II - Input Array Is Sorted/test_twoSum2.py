from twoSum2 import Solution
import pytest


cases = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
    ([0, 0, 3, 4], 0, [1, 2]),
    ([3, 3], 6, [1, 2]),
]


@pytest.mark.parametrize("numbers,target,expected", cases)
def test__Solution__twoSum2(numbers, target, expected):
    sol = Solution()
    assert expected == sol.twoSum2(numbers, target)
