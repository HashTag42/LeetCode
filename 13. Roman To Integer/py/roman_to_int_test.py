import json
import pathlib
import pytest
from roman_to_int import Solution

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "roman_to_int_test_cases.json"

with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('s, expected', test_cases)
def test_roman_to_int(s, expected):
    assert Solution().roman_to_int(s) == expected


def test_roman_to_int_exception():
    with pytest.raises(ValueError):
        Solution().roman_to_int("INVALID")
