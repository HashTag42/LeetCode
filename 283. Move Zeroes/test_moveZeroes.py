from moveZeroes import Solution
import pytest


cases = [
    ([0], [0]),
    ([0, 1], [1, 0]),
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
]


@pytest.mark.parametrize("nums, expected", cases)
def test__moveZeroes__(nums, expected):
    solution = Solution()
    solution.moveZeroes(nums)
    assert nums == expected
