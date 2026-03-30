import json
import pathlib
import pytest
from majorityElement import Solution

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"
with open(test_cases_path) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize("nums, expected", test_cases)
def test__majorityElement__(nums, expected):
    assert Solution().majorityElement(nums) is expected
