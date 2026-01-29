import json
import pathlib
import pytest
from RecentCounter import RecentCounter

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"

with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('inputs, expected', test_cases)
def test_RecentCounter_example(inputs, expected):
    rc = RecentCounter()
    result = [rc.ping(t) for t in inputs]
    assert result == expected
