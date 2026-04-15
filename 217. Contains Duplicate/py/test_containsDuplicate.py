import json
import pathlib
import pytest
from containsDuplicate import Solution

test_cases_path = pathlib.Path(__file__).resolve().parents[1] / "test_cases.json"
with open(test_cases_path) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize("nums, expected", test_cases)
def test__containsDuplicate(nums, expected):
    solution = Solution()
    assert solution.containsDuplicate(nums) == expected
