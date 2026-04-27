import json
import pathlib
import pytest
from missingNumber import Solution

test_cases_path = pathlib.Path(__file__).resolve().parents[1] / "test_cases.json"
with open(test_cases_path) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize("nums,expected", test_cases)
def test__Solution_missingNumber1(nums, expected):
    sol = Solution()
    assert expected == sol.missingNumber1(nums)


@pytest.mark.parametrize("nums,expected", test_cases)
def test__Solution_missingNumber2(nums, expected):
    sol = Solution()
    assert expected == sol.missingNumber2(nums)
