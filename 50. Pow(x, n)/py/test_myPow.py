import json
import pathlib
import pytest
from myPow import Solution


root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"
with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize("x, n, expected", test_cases)
def test__myPow__(x, n, expected):
    solution = Solution()
    assert pytest.approx(solution.myPow(x, n)) == expected
