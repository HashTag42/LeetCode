from containsDuplicate import Solution
import pytest


cases = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
]


@pytest.mark.parametrize("nums, expected", cases)
def test__containsDuplicate(nums, expected):
    solution = Solution()
    assert solution.containsDuplicate(nums) == expected
