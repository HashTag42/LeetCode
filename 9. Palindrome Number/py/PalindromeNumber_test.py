import json
import pathlib
import pytest
from PalindromeNumber import Solution

root = pathlib.Path(__file__).resolve().parents[1]

test_cases_path = root / "test_cases.json"

with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('x, expected', test_cases)
def test_isPalindrome(x, expected):
    sol = Solution()
    actual = "true" if sol.isPalindrome(x) is True else "false"
    assert actual == expected
