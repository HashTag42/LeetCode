import json
import os

import pytest
from PascalTriangle import Solution

_TEST_CASES_PATH = os.path.join(os.path.dirname(__file__), "..", "test_cases.json")

with open(_TEST_CASES_PATH) as f:
    _TEST_CASES = json.load(f)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("case", _TEST_CASES, ids=[str(c["numRows"]) for c in _TEST_CASES])
def test_generate(solution, case):
    assert solution.generate(case["numRows"]) == case["expected"]
