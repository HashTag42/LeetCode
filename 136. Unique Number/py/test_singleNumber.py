import json
import pathlib
import pytest
from singleNumber import Solution

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test" / "test_cases.json"
with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize("nums, expected", test_cases)
def test_Solution_singleNumber(nums, expected):
    assert Solution().singleNumber(nums) == expected
