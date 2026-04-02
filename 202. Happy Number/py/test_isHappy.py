import json
import pathlib
import pytest
from isHappy import Solution

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"
with open(test_cases_path) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize("n, expected", test_cases)
def test__isHappy__(n, expected):
    solution = Solution()
    assert solution.isHappy(n) == expected
