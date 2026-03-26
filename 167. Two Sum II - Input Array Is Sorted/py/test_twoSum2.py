import json
import pathlib
import pytest
from twoSum2 import Solution

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test" / "test_cases.json"
with open(test_cases_path) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize("numbers,target,expected", test_cases)
def test__Solution__twoSum2(numbers, target, expected):
    assert Solution().twoSum2(numbers, target) == expected
