import json
import pathlib
import pytest
from climbStairs import Solution

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"
with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('x, expected', test_cases)
def test_climbStairs(x, expected):
    assert Solution().climbStairs(x) == expected
