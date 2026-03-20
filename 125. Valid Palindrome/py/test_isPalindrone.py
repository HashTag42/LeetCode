import json
import pathlib
import pytest
from isPalindrome import Solution


root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test" / "testcase_data.json"
with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize("s, expected", test_cases)
def test__isPalindrome1__(s, expected):
    solution = Solution()
    assert solution.isPalindrome1(s) == expected


@pytest.mark.parametrize("s, expected", test_cases)
def test__isPalindrome2__(s, expected):
    solution = Solution()
    assert solution.isPalindrome2(s) == expected
