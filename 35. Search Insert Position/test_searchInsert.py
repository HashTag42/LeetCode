from searchInsert import Solution
import pytest


cases = [
    # nums, target, expected
    ([1, 3, 5, 6], 0, 0),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 7, 4),
]


@pytest.mark.parametrize("nums, target, expected", cases)
def test_Solution_searchInsert(nums, target, expected):
    assert Solution().searchInsert(nums, target) == expected
