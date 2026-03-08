import json
import pathlib
import pytest
from searchInsert import Solution


root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"
with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('nums, target, expected', test_cases)
def test_searchInsert(nums, target, expected):
    assert Solution().searchInsert(nums, target) == expected
