import json
import pathlib
import pytest
from moveZeroes import Solution

test_cases_path = pathlib.Path(__file__).resolve().parents[1] / "test_cases.json"
with open(test_cases_path) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize("nums, expected", test_cases)
def test__moveZeroes__(nums, expected):
    solution = Solution()
    solution.moveZeroes(nums)
    assert nums == expected


def test__moveZeroes__mutates_in_place():
    nums = [0, 1, 0, 3, 12]
    nums_id_before = id(nums)

    solution = Solution()
    solution.moveZeroes(nums)

    assert id(nums) == nums_id_before
    assert nums == [1, 3, 12, 0, 0]
