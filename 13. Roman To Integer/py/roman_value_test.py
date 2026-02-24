import json
import pathlib
import pytest
from roman_to_int import Solution

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "roman_value_test_cases.json"

with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('s, expected', test_cases)
def test_roman_value(s, expected):
    sol = Solution()
    assert sol.roman_value(s) == expected
