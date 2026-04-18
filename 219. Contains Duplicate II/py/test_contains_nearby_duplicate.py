import json
import pathlib
import pytest
from contains_nearby_duplicate import contains_nearby_duplicate

test_cases_path = pathlib.Path(__file__).resolve().parents[1] / "test_cases.json"
with open(test_cases_path) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize('nums, k, expected', test_cases)
def test_contains_nearby_duplicate(nums, k, expected):
    assert contains_nearby_duplicate(nums, k) == expected
