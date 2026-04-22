import json
import pathlib
import pytest
from isAnagram import Solution

test_cases_path = pathlib.Path(__file__).resolve().parents[1] / "test_cases.json"
with open(test_cases_path) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize("s, t, expected", test_cases)
def test__isAnagram__(s, t, expected):
    solution = Solution()
    assert solution.isAnagram(s, t) == expected
