import json
import pathlib
import pytest
from isPowerOfTwo import Solution

test_cases_path = pathlib.Path(__file__).resolve().parents[1] / "test_cases.json"
with open(test_cases_path) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize("n, expected", test_cases)
def test_Solution_isPowerOfTwo(n, expected):
    assert Solution().isPowerOfTwo(n) == expected
