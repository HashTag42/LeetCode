import json
import pathlib
import pytest
from BestTimetoBuyandSellStock import Solution


root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test" / "testcase_data.json"
with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('prices, expected', test_cases)
def test_maxProfit(prices, expected):
    assert Solution().maxProfit(prices) == expected
