import json
import pathlib
import pytest
from length_of_last_word import Solution

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"

with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('s, expected', test_cases)
def test_guess_number(s, expected):
    sol = Solution()
    assert sol.length_of_last_word(s) == expected
