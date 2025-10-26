from majorityElement import Solution
import pytest


cases = [
    # (nums, expected)
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([6, 5, 5], 5),
    ([-2, -1, -2], -2),
    ([-1, 0, 0, 1], 0),
]


@pytest.mark.parametrize("nums, expected", cases)
def test__majorityElement__(nums, expected):
    solution = Solution()
    assert expected == solution.majorityElement(nums)
