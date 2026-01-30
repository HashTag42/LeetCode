import json
import pathlib
import pytest
from minCostClimbingStairs import minCostClimbingStairs

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"

with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('cost, expected', test_cases)
def test_minCostClimbingStais(cost, expected):
    assert minCostClimbingStairs(cost) == expected
